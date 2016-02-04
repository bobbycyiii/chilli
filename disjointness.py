# SAGE code for disjointness
qf = qepcad_formula
var('t012,e01,e10,e12,e21')

top_c = e01*e10^2*e12^2*e21*t012 - e12^3 - 1
bot_c = e21^3*t012 + t012 - e01^2*e10*e12*e21^2
cyan_pos = qf.and_(top_c > 0, bot_c > 0)
cyan_neg = qf.and_(top_c < 0, bot_c < 0)
cyan_0   = qf.and_(top_c== 0, bot_c== 0)

top_y = e01*e10^3*e12^2*e21*t012 + e01*e12^2*e21*t012 - e10
bot_y = e01*t012 - e01^3*e10*e12*e21^2 - e10*e12*e21^2
yell_pos = qf.and_(top_y > 0, bot_y > 0)
yell_neg = qf.and_(top_y < 0, bot_y < 0)
yell_0   = qf.and_(top_y== 0, bot_y== 0)

all_pos = qf.and_(t012>0, e01>0, e10>0, e12>0, e21>0)

cyan   = qf.and_(all_pos,qf.or_(cyan_pos,cyan_0,cyan_neg))
yellow = qf.and_(all_pos,qf.or_(yell_pos,yell_0,yell_neg))

qepcad(qf.and_(cyan,yellow),solution='cell-points')
