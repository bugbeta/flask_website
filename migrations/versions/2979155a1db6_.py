"""empty message

Revision ID: 2979155a1db6
Revises: 00932cb7698c
Create Date: 2017-02-14 00:10:09.541000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2979155a1db6'
down_revision = '00932cb7698c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comments', sa.Column('pub_time', sa.DateTime(), nullable=True))
    op.create_index(op.f('ix_comments_pub_time'), 'comments', ['pub_time'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_comments_pub_time'), table_name='comments')
    op.drop_column('comments', 'pub_time')
    # ### end Alembic commands ###
