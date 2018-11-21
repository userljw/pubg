#encoding=utf-8

class Player(object):

    def __init__(self, id, teamId, teamName, pos, life, attack, sight, status, damageRatio):
        self.id = id                    #玩家id
        self.teamId = teamId            #玩家所属队伍的teamId
        self.teamName = teamName        #玩家所属队伍的teamName
        self.pos = pos                  #玩家当前位置pos
        self.life = life                #玩家当前生命值life
        self.attack = attack            #玩家当前攻击力attack
        self.sight = sight              #玩家当前视野大小sight
        self.status = status            #玩家状态status 0－死亡，1-存活
        self.damageRatio = damageRatio  #玩家的受伤害系数，初始值为1，每轮结束归1

    def get_position(self):
        return (self.pos)

    def move_LEFT(self):
        self.pos = self.pos - 1

    def move_RIGHT(self):
        self.pos = self.pos + 1
