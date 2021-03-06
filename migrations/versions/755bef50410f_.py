"""empty message

Revision ID: 755bef50410f
Revises: 11630d789d73
Create Date: 2017-02-26 19:03:29.342000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '755bef50410f'
down_revision = '11630d789d73'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('profiles', sa.Column('cover', sa.String(length=64), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('profiles', 'cover')
    # ### end Alembic commands ###
