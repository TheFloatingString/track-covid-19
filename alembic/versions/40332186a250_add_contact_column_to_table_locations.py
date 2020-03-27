"""add contact column to table locations

Revision ID: 40332186a250
Revises: 17d55cfe7fe7
Create Date: 2020-03-23 12:40:08.863795

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '40332186a250'
down_revision = '17d55cfe7fe7'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column(
    	"locations",
    	sa.Column("contact", sa.String))

def downgrade():
    pass
