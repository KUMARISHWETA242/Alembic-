from sqlalchemy import Integer, String, DateTime , Boolean
from sqlalchemy.orm import DeclarativeBase, mapped_column , Mapped

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ ="users"

    id :Mapped[int] = mapped_column(Integer, primary_key=True)
    username :Mapped[str] = mapped_column(String,nullable=False)
    email :Mapped[str] = mapped_column(String, nullable=False)
    address :Mapped[str] = mapped_column(String)


    

