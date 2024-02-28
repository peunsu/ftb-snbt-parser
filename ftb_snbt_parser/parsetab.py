
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'BOOL BYTE COLON COMMA DOUBLE INTEGER LBRACE LBRACKET LONG NAME RBRACE RBRACKET STRINGsnbt : compoundcompound : LBRACE key_value_pairs RBRACE\n                | LBRACE RBRACEkey_value_pairs : key_value_pairs key_value_pair\n                       | key_value_pairs COMMA key_value_pair\n                       | key_value_pairkey_value_pair : NAME COLON value\n                      | STRING COLON valuevalue : compound\n                | list\n                | BOOL\n                | BYTE\n                | DOUBLE\n                | LONG\n                | INTEGER\n                | STRINGlist : LBRACKET values RBRACKET\n                | LBRACKET RBRACKETvalues : values value\n              | values COMMA value\n              | value'
    
_lr_action_items = {'LBRACE':([0,5,9,12,13,16,17,18,19,20,21,22,23,24,26,27,28,29,30,31,32,],[3,-3,-2,3,3,-9,-10,-11,-12,-13,-14,-15,-16,3,3,-18,-21,-17,-19,3,-20,]),'$end':([1,2,5,9,],[0,-1,-3,-2,]),'RBRACE':([3,4,5,6,9,10,14,15,16,17,18,19,20,21,22,23,25,27,29,],[5,9,-3,-6,-2,-4,-5,-7,-9,-10,-11,-12,-13,-14,-15,-16,-8,-18,-17,]),'NAME':([3,4,5,6,9,10,11,14,15,16,17,18,19,20,21,22,23,25,27,29,],[7,7,-3,-6,-2,-4,7,-5,-7,-9,-10,-11,-12,-13,-14,-15,-16,-8,-18,-17,]),'STRING':([3,4,5,6,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,],[8,8,-3,-6,-2,-4,8,23,23,-5,-7,-9,-10,-11,-12,-13,-14,-15,-16,23,-8,23,-18,-21,-17,-19,23,-20,]),'COMMA':([4,5,6,9,10,14,15,16,17,18,19,20,21,22,23,25,26,27,28,29,30,32,],[11,-3,-6,-2,-4,-5,-7,-9,-10,-11,-12,-13,-14,-15,-16,-8,31,-18,-21,-17,-19,-20,]),'RBRACKET':([5,9,16,17,18,19,20,21,22,23,24,26,27,28,29,30,32,],[-3,-2,-9,-10,-11,-12,-13,-14,-15,-16,27,29,-18,-21,-17,-19,-20,]),'BOOL':([5,9,12,13,16,17,18,19,20,21,22,23,24,26,27,28,29,30,31,32,],[-3,-2,18,18,-9,-10,-11,-12,-13,-14,-15,-16,18,18,-18,-21,-17,-19,18,-20,]),'BYTE':([5,9,12,13,16,17,18,19,20,21,22,23,24,26,27,28,29,30,31,32,],[-3,-2,19,19,-9,-10,-11,-12,-13,-14,-15,-16,19,19,-18,-21,-17,-19,19,-20,]),'DOUBLE':([5,9,12,13,16,17,18,19,20,21,22,23,24,26,27,28,29,30,31,32,],[-3,-2,20,20,-9,-10,-11,-12,-13,-14,-15,-16,20,20,-18,-21,-17,-19,20,-20,]),'LONG':([5,9,12,13,16,17,18,19,20,21,22,23,24,26,27,28,29,30,31,32,],[-3,-2,21,21,-9,-10,-11,-12,-13,-14,-15,-16,21,21,-18,-21,-17,-19,21,-20,]),'INTEGER':([5,9,12,13,16,17,18,19,20,21,22,23,24,26,27,28,29,30,31,32,],[-3,-2,22,22,-9,-10,-11,-12,-13,-14,-15,-16,22,22,-18,-21,-17,-19,22,-20,]),'LBRACKET':([5,9,12,13,16,17,18,19,20,21,22,23,24,26,27,28,29,30,31,32,],[-3,-2,24,24,-9,-10,-11,-12,-13,-14,-15,-16,24,24,-18,-21,-17,-19,24,-20,]),'COLON':([7,8,],[12,13,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'snbt':([0,],[1,]),'compound':([0,12,13,24,26,31,],[2,16,16,16,16,16,]),'key_value_pairs':([3,],[4,]),'key_value_pair':([3,4,11,],[6,10,14,]),'value':([12,13,24,26,31,],[15,25,28,30,32,]),'list':([12,13,24,26,31,],[17,17,17,17,17,]),'values':([24,],[26,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> snbt","S'",1,None,None,None),
  ('snbt -> compound','snbt',1,'p_snbt','parse.py',6),
  ('compound -> LBRACE key_value_pairs RBRACE','compound',3,'p_compound','parse.py',10),
  ('compound -> LBRACE RBRACE','compound',2,'p_compound','parse.py',11),
  ('key_value_pairs -> key_value_pairs key_value_pair','key_value_pairs',2,'p_key_value_pairs','parse.py',18),
  ('key_value_pairs -> key_value_pairs COMMA key_value_pair','key_value_pairs',3,'p_key_value_pairs','parse.py',19),
  ('key_value_pairs -> key_value_pair','key_value_pairs',1,'p_key_value_pairs','parse.py',20),
  ('key_value_pair -> NAME COLON value','key_value_pair',3,'p_key_value_pair','parse.py',29),
  ('key_value_pair -> STRING COLON value','key_value_pair',3,'p_key_value_pair','parse.py',30),
  ('value -> compound','value',1,'p_value','parse.py',34),
  ('value -> list','value',1,'p_value','parse.py',35),
  ('value -> BOOL','value',1,'p_value','parse.py',36),
  ('value -> BYTE','value',1,'p_value','parse.py',37),
  ('value -> DOUBLE','value',1,'p_value','parse.py',38),
  ('value -> LONG','value',1,'p_value','parse.py',39),
  ('value -> INTEGER','value',1,'p_value','parse.py',40),
  ('value -> STRING','value',1,'p_value','parse.py',41),
  ('list -> LBRACKET values RBRACKET','list',3,'p_list','parse.py',45),
  ('list -> LBRACKET RBRACKET','list',2,'p_list','parse.py',46),
  ('values -> values value','values',2,'p_values','parse.py',53),
  ('values -> values COMMA value','values',3,'p_values','parse.py',54),
  ('values -> value','values',1,'p_values','parse.py',55),
]
