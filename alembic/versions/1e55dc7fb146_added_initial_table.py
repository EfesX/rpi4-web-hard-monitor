"""Added initial table

Revision ID: 1e55dc7fb146
Revises: 8147de950ea4
Create Date: 2022-09-01 22:38:27.384050

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1e55dc7fb146'
down_revision = '8147de950ea4'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('temperature',
    sa.Column('temp', sa.Integer(), nullable=False),
    sa.Column('datetime', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('temp')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('temperature')
    # ### end Alembic commands ###
