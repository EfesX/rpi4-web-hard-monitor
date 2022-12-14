"""Added initial table

Revision ID: 8147de950ea4
Revises: 997378f261f5
Create Date: 2022-09-01 22:35:43.350203

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8147de950ea4'
down_revision = '997378f261f5'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('temperature')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('temperature',
    sa.Column('temp', sa.BIGINT(), autoincrement=True, nullable=False),
    sa.PrimaryKeyConstraint('temp', name='temperature_pkey')
    )
    # ### end Alembic commands ###
