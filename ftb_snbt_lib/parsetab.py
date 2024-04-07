
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'BOOL BYTE COLON COMMA DOUBLE FLOAT INTEGER LBRACE LBRACKET LONG NAME RBRACE RBRACKET SEMICOLON SHORT STRINGsnbt : compoundcompound : LBRACE key_value_pairs RBRACE\n                | LBRACE RBRACEkey_value_pairs : key_value_pairs key_value_pair\n                       | key_value_pairs COMMA key_value_pair\n                       | key_value_pairkey_value_pair : NAME COLON value\n                      | STRING COLON valuevalue : compound\n                | list\n                | array\n                | BOOL\n                | BYTE\n                | SHORT\n                | FLOAT\n                | DOUBLE\n                | LONG\n                | INTEGER\n                | STRINGlist : LBRACKET values RBRACKET\n                | LBRACKET RBRACKETarray : LBRACKET NAME SEMICOLON values RBRACKET\n                | LBRACKET NAME SEMICOLON RBRACKETvalues : values value\n              | values COMMA value\n              | value'
    
_lr_action_items = {'LBRACE':([0,5,9,12,13,16,17,18,19,20,21,22,23,24,25,26,27,29,30,32,33,34,35,36,37,38,39,40,],[3,-3,-2,3,3,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,3,3,-21,-26,-20,-24,3,3,-25,3,-23,-22,]),'$end':([1,2,5,9,],[0,-1,-3,-2,]),'RBRACE':([3,4,5,6,9,10,14,15,16,17,18,19,20,21,22,23,24,25,26,28,30,33,39,40,],[5,9,-3,-6,-2,-4,-5,-7,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-8,-21,-20,-23,-22,]),'NAME':([3,4,5,6,9,10,11,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,30,33,39,40,],[7,7,-3,-6,-2,-4,7,-5,-7,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,31,-8,-21,-20,-23,-22,]),'STRING':([3,4,5,6,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,32,33,34,35,36,37,38,39,40,],[8,8,-3,-6,-2,-4,8,26,26,-5,-7,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,26,-8,26,-21,-26,-20,-24,26,26,-25,26,-23,-22,]),'COMMA':([4,5,6,9,10,14,15,16,17,18,19,20,21,22,23,24,25,26,28,29,30,32,33,34,37,38,39,40,],[11,-3,-6,-2,-4,-5,-7,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-8,35,-21,-26,-20,-24,-25,35,-23,-22,]),'RBRACKET':([5,9,16,17,18,19,20,21,22,23,24,25,26,27,29,30,32,33,34,36,37,38,39,40,],[-3,-2,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,30,33,-21,-26,-20,-24,39,-25,40,-23,-22,]),'BOOL':([5,9,12,13,16,17,18,19,20,21,22,23,24,25,26,27,29,30,32,33,34,35,36,37,38,39,40,],[-3,-2,19,19,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,19,19,-21,-26,-20,-24,19,19,-25,19,-23,-22,]),'BYTE':([5,9,12,13,16,17,18,19,20,21,22,23,24,25,26,27,29,30,32,33,34,35,36,37,38,39,40,],[-3,-2,20,20,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,20,20,-21,-26,-20,-24,20,20,-25,20,-23,-22,]),'SHORT':([5,9,12,13,16,17,18,19,20,21,22,23,24,25,26,27,29,30,32,33,34,35,36,37,38,39,40,],[-3,-2,21,21,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,21,21,-21,-26,-20,-24,21,21,-25,21,-23,-22,]),'FLOAT':([5,9,12,13,16,17,18,19,20,21,22,23,24,25,26,27,29,30,32,33,34,35,36,37,38,39,40,],[-3,-2,22,22,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,22,22,-21,-26,-20,-24,22,22,-25,22,-23,-22,]),'DOUBLE':([5,9,12,13,16,17,18,19,20,21,22,23,24,25,26,27,29,30,32,33,34,35,36,37,38,39,40,],[-3,-2,23,23,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,23,23,-21,-26,-20,-24,23,23,-25,23,-23,-22,]),'LONG':([5,9,12,13,16,17,18,19,20,21,22,23,24,25,26,27,29,30,32,33,34,35,36,37,38,39,40,],[-3,-2,24,24,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,24,24,-21,-26,-20,-24,24,24,-25,24,-23,-22,]),'INTEGER':([5,9,12,13,16,17,18,19,20,21,22,23,24,25,26,27,29,30,32,33,34,35,36,37,38,39,40,],[-3,-2,25,25,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,25,25,-21,-26,-20,-24,25,25,-25,25,-23,-22,]),'LBRACKET':([5,9,12,13,16,17,18,19,20,21,22,23,24,25,26,27,29,30,32,33,34,35,36,37,38,39,40,],[-3,-2,27,27,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,27,27,-21,-26,-20,-24,27,27,-25,27,-23,-22,]),'COLON':([7,8,],[12,13,]),'SEMICOLON':([31,],[36,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'snbt':([0,],[1,]),'compound':([0,12,13,27,29,35,36,38,],[2,16,16,16,16,16,16,16,]),'key_value_pairs':([3,],[4,]),'key_value_pair':([3,4,11,],[6,10,14,]),'value':([12,13,27,29,35,36,38,],[15,28,32,34,37,32,34,]),'list':([12,13,27,29,35,36,38,],[17,17,17,17,17,17,17,]),'array':([12,13,27,29,35,36,38,],[18,18,18,18,18,18,18,]),'values':([27,36,],[29,38,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> snbt","S'",1,None,None,None),
  ('snbt -> compound','snbt',1,'p_snbt','parse.py',8),
  ('compound -> LBRACE key_value_pairs RBRACE','compound',3,'p_compound','parse.py',12),
  ('compound -> LBRACE RBRACE','compound',2,'p_compound','parse.py',13),
  ('key_value_pairs -> key_value_pairs key_value_pair','key_value_pairs',2,'p_key_value_pairs','parse.py',20),
  ('key_value_pairs -> key_value_pairs COMMA key_value_pair','key_value_pairs',3,'p_key_value_pairs','parse.py',21),
  ('key_value_pairs -> key_value_pair','key_value_pairs',1,'p_key_value_pairs','parse.py',22),
  ('key_value_pair -> NAME COLON value','key_value_pair',3,'p_key_value_pair','parse.py',31),
  ('key_value_pair -> STRING COLON value','key_value_pair',3,'p_key_value_pair','parse.py',32),
  ('value -> compound','value',1,'p_value','parse.py',36),
  ('value -> list','value',1,'p_value','parse.py',37),
  ('value -> array','value',1,'p_value','parse.py',38),
  ('value -> BOOL','value',1,'p_value','parse.py',39),
  ('value -> BYTE','value',1,'p_value','parse.py',40),
  ('value -> SHORT','value',1,'p_value','parse.py',41),
  ('value -> FLOAT','value',1,'p_value','parse.py',42),
  ('value -> DOUBLE','value',1,'p_value','parse.py',43),
  ('value -> LONG','value',1,'p_value','parse.py',44),
  ('value -> INTEGER','value',1,'p_value','parse.py',45),
  ('value -> STRING','value',1,'p_value','parse.py',46),
  ('list -> LBRACKET values RBRACKET','list',3,'p_list','parse.py',50),
  ('list -> LBRACKET RBRACKET','list',2,'p_list','parse.py',51),
  ('array -> LBRACKET NAME SEMICOLON values RBRACKET','array',5,'p_array','parse.py',58),
  ('array -> LBRACKET NAME SEMICOLON RBRACKET','array',4,'p_array','parse.py',59),
  ('values -> values value','values',2,'p_values','parse.py',66),
  ('values -> values COMMA value','values',3,'p_values','parse.py',67),
  ('values -> value','values',1,'p_values','parse.py',68),
]
