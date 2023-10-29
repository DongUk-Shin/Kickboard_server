"""empty message

Revision ID: 804347913b03
Revises: 9a7bd6dc47f4
Create Date: 2023-10-29 23:37:10.220386

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '804347913b03'
down_revision = '9a7bd6dc47f4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('ride_log',
    sa.Column('email', sa.Text(), nullable=False),
    sa.Column('date', sa.Text(), nullable=True),
    sa.Column('distance', sa.Text(), nullable=True),
    sa.Column('runtime', sa.Text(), nullable=True),
    sa.Column('cost', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('email')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('ride_log')
    # ### end Alembic commands ###
