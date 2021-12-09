ig = ['の', 'に', 'は', 'を', 'た', 'が', 'で', 'て', 'と', 'し', 'れ', 'さ',
  'ある', 'いる', 'も', 'する', 'から', 'な', 'こと', 'として', 'い', 'や', 'れる',
  'など', 'なっ', 'ない', 'この', 'ため', 'その', 'あっ', 'よう', 'また', 'もの',
  'という', 'あり', 'まで', 'られ', 'なる', 'へ', 'か', 'だ', 'これ', 'によって',
  'により', 'おり', 'より', 'による', 'ず', 'なり', 'られる', 'において', 'ば', 'なかっ',
  'なく', 'しかし', 'について', 'せ', 'だっ', 'その後', 'できる', 'それ', 'う', 'ので',
  'なお', 'のみ', 'でき', 'き', 'つ', 'における', 'および', 'いう', 'さらに', 'でも',
  'ら', 'たり', 'その他', 'に関する', 'たち', 'ます', 'ん', 'なら', 'に対して', '特に',
  'せる', '及び', 'これら', 'とき', 'では', 'にて', 'ほか', 'ながら', 'うち', 'そして',
  'とともに', 'ただし', 'かつて', 'それぞれ', 'または', 'お', 'ほど', 'ものの', 'に対する',
  'ほとんど', 'と共に', 'といった', 'です', 'とも', 'ところ', 'ここ', '以上', '方法', '他', '以下', '項',
  '℃', '℃、', 'μm', "%", '〕', '(','実施例', '凸', '凹', '上記', '工程', '過程', 'ρ', 'φ', '法', 'mm', 'mm×','kg', 'cm', '=', '処理', 'α' ,
'ά'	,
'Α'	,
'Ά'	,
'β'	,
'ϐ'	,
'Β'	,
'γ'	,
'Γ'	,
'δ'	,
'Δ'	,
'ε'	,
'έ'	,
'ϵ'	,
'϶'	,
'Ε'	,
'Έ'	,
'ζ'	,
'Ζ'	,
'η'	,
'ή' ,
'Η' ,
'Ή'	,
'θ'	,
'ϑ'	,
'Θ'	,
'ϴ'	,
'ι'	,
'ί'	,
'ϊ'	,
'ΐ'	,
'Ι'	,
'Ϊ'	,
'Ί'	,
'λ'	,
'Λ'	,
'μ'	,
'Μ' , 
'ν'	,
'Ν'	,
'ξ'	,
'Ξ'	,
'ο'	,
'ό'	,
'Ο'	,
'Ό'	,
'π'	,
'ϖ'	,
'Π'	,
'ρ' ,
'Ρ'	, 
'σ'	,
'ς'	,
'ϲ'	,
'ͻ'	,
'ͼ'	,
'ͽ'	,
'Σ'	,
'Ϲ'	,
'Ͻ'	,
'Ͼ'	,
'Ͽ'	,
'τ'	,
'Τ'	,
'υ'	,
'ϋ'	,
'ύ'	,
'ΰ'	,
'ϒ'	,
'Υ'	,
'Ϋ'	,
'Ύ'	,
'φ'	,
'ϕ'	,
'Φ'	,
'χ'	,
'Χ'	,
'ψ'	,
'Ψ'	,
'ω'	,
'ώ'	,
'Ω'	,
'Ώ'	,
'H'	
'He',
'Li',
'Be',
'B',	
'C',	
'N',	
'O',	
'F',	
'Ne',
'Na',
'Mg',
'Al',
'Si',
'P',	
'S',	
'Cl',
'Ar',
'K',	
'Ca',
'Sc',
'Ti',
'V',	
'Cr',
'Mn',
'Fe',
'Co',
'Ni',
'Cu',
'Zn',
'Ga',
'Ge',
'As',
'Se',
'Br',
'Kr',
'Rb',
'Sr',
'Y',	
'Zr',
'Nb',
'Mo',
'Tc',
'Ru',
'Rh',
'Pd',
'Ag',
'Cd',
'In',
'Sn',
'Sb',
'Te',
'I',	
'Xe',
'Cs',
'Ba',
'La',
'Ce',
'Pr',
'Nd',
'Pm',
'Sm',
'Eu',
'Gd',
'Tb',
'Dy',
'Ho',
'Er',
'Tm',
'Yb',
'Lu',
'Hf',
'Ta',
'W',	
'Re',
'Os',
'Ir',
'Pt',
'Au',
'Hg',
'Tl',
'Pb',
'Bi',
'Po',
'At',
'Rn',
'Fr',
'Ra',
'Ac',
'Th',
'Pa',
'U',	
'Np',
'Pu',
'Am',
'Cm',
'Bk',
'Cf',
'Es',
'Fm',
'Md',
'No',
'Lr',
'Rf',
'Db',
'Sg',
'Bh',
'Hs',
'Mt',
'Ds',
'Rg',
'Cn',
'Uu',	
'Fl',
'Uu',	
'Lv',
'Uu',	
'Uuo']


import re
def get_regex():
  p = re.compile("[ぁ 法 あ ぃ い ぅ う ぇ え ぉ 々 お か が き ぎ く ぐ け げ こ ご さ ざ し じ す ず せ ぜ そ ぞ た だ ち ぢ っ つ づ て で と ど な に ぬ ね の は ば ぱ ひ び ぴ ふ ぶ ぷ へ べ ぺ ほ ぼ ぽ ま み む め も ゃ や ゅ ゆ ょ よ ら り る れ ろ ゎ わ ゐ ゑ を ん ゔ ゕ ゖ  ゙ ゚ ゛ ゜ ゝ ゞ ゟ ゠ ァ ア ィ イ ゥ ウ ェ エ ォ オ カ ガ キ ギ ク グ ケ ゲ コ ゴ サ ザ シ ジ ス ズ セ ゼ ソ ゾ タ ダ チ ヂ ッ ツ ヅ テ デ ト ド ナ ニ ヌ ネ ノ ハ バ パ ヒ ビ ピ フ ブ プ ヘ ベ ペ ホ ボ ポ マ ミ ム メ モ ャ ヤ ュ ユ ョ ヨ ラ リ ル レ ロ ヮ ワ ヰ ヱ ヲ ン ヴ ヵ ヶ ヷ ヸ ヹ ヺ ・ ー ヽ ヾ ヿ]")
  return p

#実 装 例 物 側 装