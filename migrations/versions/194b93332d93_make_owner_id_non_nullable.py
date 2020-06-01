"""Make owner_id non-nullable

Revision ID: 194b93332d93
Revises: 12187fd04aa5
Create Date: 2020-06-01 01:27:45.860721

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '194b93332d93'
down_revision = '12187fd04aa5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('classes', 'owner_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('classes', 'owner_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###
