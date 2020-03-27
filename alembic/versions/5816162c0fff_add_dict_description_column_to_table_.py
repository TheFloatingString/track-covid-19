"""add dict_description column to table anxieties

Revision ID: 5816162c0fff
Revises: 37b8c237829a
Create Date: 2020-03-23 18:03:49.663347

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5816162c0fff'
down_revision = '37b8c237829a'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column(
    	"anxieties",
    	sa.Column("dict_description", sa.types.PickleType))


def downgrade():
    pass
