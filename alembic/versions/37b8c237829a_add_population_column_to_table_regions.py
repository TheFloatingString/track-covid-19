"""add population column to table regions

Revision ID: 37b8c237829a
Revises: 40332186a250
Create Date: 2020-03-23 16:08:22.731480

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '37b8c237829a'
down_revision = '40332186a250'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column(
    	"regions",
    	sa.Column("population", sa.Integer))

def downgrade():
    pass
