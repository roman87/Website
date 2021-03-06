"""Art

Revision ID: 5aec407f2ab5
Revises: 
Create Date: 2018-11-12 13:17:43.981491

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5aec407f2ab5'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('art',
    sa.Column('ids', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=256), nullable=True),
    sa.Column('text', sa.String(length=2048), nullable=True),
    sa.PrimaryKeyConstraint('ids')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('art')
    # ### end Alembic commands ###
