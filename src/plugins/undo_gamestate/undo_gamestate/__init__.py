"""
This is where the implementation of the plugin code goes.
The undo_gamestate-class is imported from both run_plugin.py and run_debug.py
"""
import sys
import logging
from webgme_bindings import PluginBase

# Setup a logger
logger = logging.getLogger('undo_gamestate')
logger.setLevel(logging.INFO)
handler = logging.StreamHandler(sys.stdout)  # By default it logs to stderr..
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)


class undo_gamestate(PluginBase):
  def main(self):
    active_node = self.active_node
    core = self.core
    logger = self.logger
    self.namespace = None
    META = self.META
    logger.debug('path: {0}'.format(core.get_path(active_node)))
    logger.info('name: {0}'.format(core.get_attribute(active_node, 'name')))
    logger.warn('pos : {0}'.format(core.get_registry(active_node, 'position')))
    logger.error('guid: {0}'.format(core.get_guid(active_node)))
    nodesList = core.load_sub_tree(active_node)
    
    nodes = {}
    game_states=[]
    for node in nodesList:
      nodes[core.get_path(node)] = node
    for path in nodes:
      node = nodes[path]
      game_state = {}
      if (core.is_instance_of(node, META['GameState'])):
        game_state['name']=core.get_attribute(node, 'name')
        game_state['path'] = path
        game_states.append(game_state)
        
        currentplayer_path = core.get_pointer_path(node,'currentPlayer')
        player = nodes[currentplayer_path]
        game_state['currentplayer'] = core.get_attribute(player,'name')
        
        currentplayer_move = core.get_pointer_path(node, 'currentMove')
        playermove = nodes[currentplayer_move]
        currentmove = {}
        currentmove['color']=core.get_attribute(playermove,'color')
        currentmove['row']=core.get_attribute(core.get_parent(playermove),'row')
        currentmove['column']=core.get_attribute(core.get_parent(playermove),'column')
        game_state['currentmove'] = currentmove
        
        #logger.info(game_states)
        rows = 8
        column = 8
        board = [[0 for _ in range(column)] for _ in range(rows)]
        game_state["board"] = board
        
      
      
      if (core.is_instance_of(node,META['Tile'])):
        for game_state in game_states:
          if game_state["path"][:4] == path[:4]:
            row = core.get_attribute(node,'row')
            column = core.get_attribute(node,'column')
            children = core.get_children_paths(node)
            flips = []
            childcolor = None
            childpath = None
            if len(children)>0:
              childpath = children[0]
              childcolor = core.get_attribute(nodes[childpath],'color')
              for otherpath in nodes:
                othernode = nodes[otherpath]
                if(core.is_instance_of(othernode,META['mightFlip'])):
                  
                  srctile=core.get_parent(nodes[core.get_pointer_path(othernode,'src')])
                  dsttile=core.get_parent(nodes[core.get_pointer_path(othernode,'dst')])
                  dstinfo = {'column': core.get_attribute(dsttile, 'column'),'row':core.get_attribute(dsttile,'row')}
                  if node == srctile:
                    flips.append(dstinfo)
    
  


            game_state["board"][row-1][column-1] = {"color":childcolor, "flips":flips}
    #logger.info(game_states)
    self.undo()
    
    
    
  def undo(self):
      active_node=self.active_node 
      core = self.core
      logger = self.logger
      self.namespace = None
      META = self.META
      nodesList = core.load_sub_tree(active_node)
    
      nodes = {}
      game_states=[]
      for node in nodesList:
        nodes[core.get_path(node)] = node
         
      current_gs_path=core.get_pointer_path(active_node,'currentGS')
      current_gs=nodes[current_gs_path]
      logger.info(core.get_attribute(current_gs,'name'))
      prev_state_path=core.get_pointer_path(current_gs,'previousGS')
      prev_state=nodes[prev_state_path]#doubtfull
      core.set_pointer(active_node,'currentGS',prev_state)
      core.delete_node(current_gs)
      self.util.save(self.root_node,self.commit_hash,self.branch_name)
      
   

