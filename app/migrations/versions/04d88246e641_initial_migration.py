"""Initial migration.

Revision ID: 04d88246e641
Revises: 
Create Date: 2022-11-08 18:06:26.958043

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '04d88246e641'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('books',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('short_desc', sa.Text(), nullable=False),
    sa.Column('rating_sum', sa.Integer(), nullable=False),
    sa.Column('rating_num', sa.Integer(), nullable=False),
    sa.Column('year', mysql.YEAR(), nullable=False),
    sa.Column('publisher', sa.String(length=100), nullable=False),
    sa.Column('author', sa.String(length=100), nullable=False),
    sa.Column('vol_pages', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_books'))
    )
    op.create_table('genres',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_genres')),
    sa.UniqueConstraint('name', name=op.f('uq_genres_name'))
    )
    op.create_table('roles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('desciption', sa.Text(), nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_roles'))
    )
    op.create_table('book_genre',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('book_id', sa.Integer(), nullable=True),
    sa.Column('genre_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['book_id'], ['books.id'], name=op.f('fk_book_genre_book_id_books'), ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['genre_id'], ['genres.id'], name=op.f('fk_book_genre_genre_id_genres'), ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_book_genre'))
    )
    op.create_table('images',
    sa.Column('id', sa.String(length=100), nullable=False),
    sa.Column('file_name', sa.String(length=100), nullable=False),
    sa.Column('mime_type', sa.String(length=100), nullable=False),
    sa.Column('md5_hash', sa.String(length=100), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.Column('book_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['book_id'], ['books.id'], name=op.f('fk_images_book_id_books'), ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_images')),
    sa.UniqueConstraint('md5_hash', name=op.f('uq_images_md5_hash'))
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('last_name', sa.String(length=100), nullable=False),
    sa.Column('first_name', sa.String(length=100), nullable=False),
    sa.Column('middle_name', sa.String(length=100), nullable=False),
    sa.Column('login', sa.String(length=100), nullable=False),
    sa.Column('password_hash', sa.String(length=200), nullable=False),
    sa.Column('role_id', sa.Integer(), nullable=True),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.ForeignKeyConstraint(['role_id'], ['roles.id'], name=op.f('fk_users_role_id_roles'), ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_users')),
    sa.UniqueConstraint('login', name=op.f('uq_users_login')),
    sa.UniqueConstraint('password_hash', name=op.f('uq_users_password_hash'))
    )
    op.create_table('reviews',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('rating', sa.Integer(), nullable=False),
    sa.Column('text', sa.Text(), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.Column('book_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['book_id'], ['books.id'], name=op.f('fk_reviews_book_id_books'), ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name=op.f('fk_reviews_user_id_users'), ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_reviews'))
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('reviews')
    op.drop_table('users')
    op.drop_table('images')
    op.drop_table('book_genre')
    op.drop_table('roles')
    op.drop_table('genres')
    op.drop_table('books')
    # ### end Alembic commands ###
