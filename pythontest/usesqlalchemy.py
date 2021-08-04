from psutil.tests.test_connections import Base
from sqlalchemy import create_engine, Column, Integer, String, Float, or_, func

# 初始化数据库连接
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('mysql+mysqlconnector://root:root@localhost:3306/nba')
Base = declarative_base()


# 增加to_dict()方法到Base类中
def to_dict(self):
    return {c.name: getattr(self, c.name, None)
            for c in self.__table__.columns}


# 将对象可以转化为dict类型
Base.to_dict = to_dict


# 定义Player对象:
class Player(Base):
    # 表的名字:
    __tablename__ = 'player'
    # 表的结构:
    player_id = Column(Integer, primary_key=True, autoincrement=True)
    team_id = Column(Integer)
    player_name = Column(String(255))
    height = Column(Float(3, 2))


# 创建DBSession类型
DBSession = sessionmaker(bind=engine)
# 创建session对象
session = DBSession()
# 创建player对象
new_player = Player(team_id=1003, player_name="涛涛1", height=2)

# #添加到session
# session.add(new_player)
# #提交即保存到数据库
# session.commit()

# 查身高大于2.08的球员
rows = session.query(Player).filter(Player.height >= 2.08).all()
print([row.to_dict() for row in rows])

rows = session.query(Player).filter(Player.height >= 2.08, Player.height <= 2.10).all()
print([row.to_dict() for row in rows])

rows = session.query(Player).filter(or_(Player.height >= 2.08, Player.height <= 2)).all()
print([row.to_dict() for row in rows])

rows = session.query(Player.team_id,
                     func.count(Player.player_id)).group_by(Player.team_id).having(
    func.count(Player.player_id) > 5).order_by(func.count(Player.player_id).asc()).all()
print(rows)
# rows=session.query(Player).filter(Player.player_name=='涛涛1').first()
# session.delete(rows)
# session.commit()
rows=session.query(Player).filter(Player.player_name=='伊凯·阿尼博古').first()
rows.height=2.09
session.commit()
# 关闭session
session.close()
