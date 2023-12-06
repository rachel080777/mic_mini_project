"""
This is where the implementation of the plugin code goes.
The highlight_tiles-class is imported from both run_plugin.py and run_debug.py
"""
import sys
import logging
from webgme_bindings import PluginBase

# Setup a logger
logger = logging.getLogger('highlight_tiles')
logger.setLevel(logging.INFO)
handler = logging.StreamHandler(sys.stdout)  # By default it logs to stderr..
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)


class highlight_tiles(PluginBase):
  def main(self):
    active_node = self.active_node
    core = self.core
    logger = self.logger
    logger.debug('path: {0}'.format(core.get_path(active_node)))
    logger.info('name: {0}'.format(core.get_attribute(active_node, 'name')))
    logger.warn('pos : {0}'.format(core.get_registry(active_node, 'position')))
    logger.error('guid: {0}'.format(core.get_guid(active_node)))
    self.namespace = None
    META = self.META
    
    nodesList = core.load_sub_tree(active_node)
    nodes = {}
    for node in nodesList:
      nodes[core.get_path(node)] = node
    self.nodes = nodes
      
    state = {}
    #for path in nodes:
      #node = nodes[path]
      #name = core.get_attribute(node, 'name')    
    name=core.get_attribute(active_node,'name')
    currentMovePath= core.get_pointer_path(active_node, "currentMove")
    currentMove=core.load_by_path(self.root_node,currentMovePath)
    currentMoveColor = core.get_attribute(currentMove,'color')
    currentMoveTile = core.get_parent(currentMove)
    currentMoveTileRow = core.get_attribute(currentMoveTile, 'row')
    currentMoveTileColumn = core.get_attribute(currentMoveTile, 'column')
    currentPlayerPath= core.get_pointer_path(active_node, "currentPlayer")
    currentPlayer=core.load_by_path(self.root_node,currentMovePath)
    currentPlayerColor = core.get_attribute(currentPlayer,'color')
    state["name"]=name
    state["board"]= [[None for x in range(8)] for x  in range(8)]
    state["currentPlayer"]= currentPlayerColor
    state["currentMoveColor"]=currentMoveColor
    state["currentMoveTileRow"]=currentMoveTile
    state["currentMoveTileColumn"]=currentMoveTileColumn
    #state.append({"name": name, "board": [[None for x in range(8)] for x  in range(8)], "currentPlayer" : currentPlayerColor,
                     #"currentMoveColor": currentMoveColor, "currentMoveTileRow": currentMoveTileRow, "currentMoveTileColumn": currentMoveTileColumn}) 
    child_paths=core.get_children_paths(active_node)
      #old_player = core.get_pointer_path(copied_node, "currentPlayer")
    for child_path in child_paths:
      child=core.load_by_path(self.root_node,child_path)
      if core.is_instance_of(child, META["Board"]):
        board = child
        tile_paths = core.get_children_paths(board)
        for tile_path in tile_paths:
          
          tile = core.load_by_path(self.root_node, tile_path)
          if core.is_instance_of(tile, META["Tile"]):                      
            row=core.get_attribute(tile,'row')
            column=core.get_attribute(tile,'column')          
            tile_children=core.get_children_paths(tile)
            for tile_child in tile_children:
               if(len(tile_child)>0):
                    piece=core.load_by_path(self.root_node,tile_child)
                    if core.is_instance_of(piece, META["Piece"]):

                      childColor=core.get_attribute(piece,'color')

                      state["board"][row][column] = {"color": childColor}
                    else:
                        state["board"][row][column] = {"color": None}

              
            
    self.state = state
    logger.info(self.state)
    #self.count_color()
    
    self.highlight_tile()
    
     
    
  def highlight_tile(self):
    valid_tiles=[]
    active_node=self.active_node 
    
    core = self.core
    logger = self.logger
    self.namespace = None
    META = self.META
    logger.info(core.get_attribute(active_node,'name'))
    '''
    nodesList = core.load_sub_tree(active_node)
    current_player = self.nodes[core.get_pointer_path(active_node, "currentPlayer")]
    current_player_color = core.get_attribute(current_player, 'color')
    logger.info(current_player_color)
    '''
    
    child_paths=core.get_children_paths(active_node)
    #old_player = core.get_pointer_path(copied_node, "currentPlayer")
    for child_path in child_paths:
      child=core.load_by_path(self.root_node,child_path)
      if core.is_instance_of(child, META["Board"]):
        board = child
        tile_paths = core.get_children_paths(board)
        for tile_path in tile_paths:
          
          tile = core.load_by_path(self.root_node, tile_path)
          if core.is_instance_of(tile,META["Tile"]):
          #logger.info("row: {0} column: {1}".format(core.get_attribute(tile,'row'),core.get_attribute(tile,'column')))
            valid=self.next_move_viable(tile)
            if valid==True:
              row=core.get_attribute(tile,'row')
              column=core.get_attribute(tile,'column')
              valid_tiles.append([row,column])
     
    logger.info(valid_tiles)
    return valid_tiles
          
  def next_move_viable(self, tile):
    self.valid = False
    self.to_flip = []
    META = self.META
    self.next_moves = {"black":"white", "white": "black"}
    flip_directions = [(0,1), (1,0), (1,1), (-1,-1), (1,-1), (-1,1), (-1,0), (0,-1)]
    logger = self.logger
    core = self.core
    current_tile=tile
    state=self.state
    
    
    
    gamestate = self.active_node
    current_player_path = core.get_pointer_path(gamestate, "currentPlayer")
    current_player = core.load_by_path(self.root_node,current_player_path)
    current_player_color = core.get_attribute(current_player, 'color')
  
    
    current_move_path = core.get_pointer_path(gamestate, "currentMove")
    current_move = core.load_by_path(self.root_node,current_move_path)
    current_move_color = core.get_attribute(current_move, 'color')
    
    
    next_move_color = self.next_moves[current_move_color]
    self.next_move_color = next_move_color
   
    board_ref=state["board"]
    
    column = core.get_attribute(current_tile, 'column')
    row = core.get_attribute(current_tile, 'row')
    
    
    if board_ref[row][column]== None:
      for direction in flip_directions:
        to_flip = []
        rows = len(board_ref)      # Number of rows in the board
        columns = len(board_ref[0]) # Number of columns in the board (assuming all rows are of equal length)

        # Calculate new indices
        new_row = row + direction[0]
        new_column = column + direction[1]

# Check if the indices are within the valid range and the position is not None
        if 0 <= new_row < rows and 0 <= new_column < columns and board_ref[new_row][new_column] is not None:
          if board_ref[row + direction[0]][column + direction[1]]!=None and board_ref[row + direction[0]][column + direction[1]]['color'] == current_move_color:
            to_flip = [(row + direction[0], column + direction[1])]
            multiplier = 2
            while (row + (direction[0]*multiplier) > 0 and row + (direction[0]*multiplier) < 8) and (column + (direction[1]*multiplier) > 0 and column + (direction[1]*multiplier) < 8) and board_ref[row + direction[0]*multiplier][column + (direction[1]*multiplier)]!=None:
              if board_ref[row + direction[0]*multiplier][column + (direction[1]*multiplier)]['color'] == next_move_color:
                end_position = (row + direction[0]*multiplier, column + (direction[1]*multiplier))
                for position in to_flip:
                  self.to_flip.append(position)
                  self.valid = True
              to_flip.append((row + direction[0]*multiplier, column + (direction[1]*multiplier)))
              multiplier +=1
    #logger.info(self.valid)
    return self.valid
  
  

  
    
    
    
    
    
    
    
    
  
  

