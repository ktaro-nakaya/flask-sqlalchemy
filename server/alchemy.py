from flask import (Flask, Blueprint, jsonify)
from sqlalchemy import create_engine, URL
from sqlalchemy.orm import sessionmaker, scoped_session, DeclarativeBase, Mapped, mapped_column


# 接続情報
url_object = URL(
    drivername='mysql+mysqlconnector',
    host='localhost',
    port=3306,
    username='root',
    password='P@ssw0rd',
    database='alchemy',
    query={"charset": "utf8"}
)

# SQLAlchemyのエンジン生成
engine = create_engine(url_object)

# DBとの接続インターフェースのsessionを生成
session = scoped_session(sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
))

bp_alchemy = Blueprint(__name__, 'bp_alchemy', url_prefix='/api/alchemy')

# マッピングするベースクラスを定義


class Base(DeclarativeBase):
    pass

# マッピングするクラスを定義


class Item(Base):
    __tablename__ = "items"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    price: Mapped[int]


@bp_alchemy.get('/')
def get_all():
    # 全件検索
    all_data = session.query(Item).all()

    # 検索結果をdict型に変換
    result = [{'id': item.id, 'name': item.name, 'price': item.price}
              for item in all_data]

    return jsonify(result), 200
