"""empty message

Revision ID: 20cba214a29e
Revises: c4050b4e8ebc
Create Date: 2022-06-14 00:11:13.023244

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '20cba214a29e'
down_revision = 'c4050b4e8ebc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('comment', schema=None) as batch_op:
        batch_op.add_column(sa.Column('create_date', sa.DateTime(), nullable=False))
        batch_op.drop_column('create_time')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('comment', schema=None) as batch_op:
        batch_op.add_column(sa.Column('create_time', sa.DATETIME(), nullable=False))
        batch_op.drop_column('create_date')

    # ### end Alembic commands ###
