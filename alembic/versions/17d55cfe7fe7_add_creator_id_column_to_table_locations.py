"""add creator_id column to table locations

Revision ID: 17d55cfe7fe7
Revises: 
Create Date: 2020-03-22 17:10:11.269314

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID



# revision identifiers, used by Alembic.
revision = '17d55cfe7fe7'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.add_column(
    	"locations",
    	sa.Column("creator_id", UUID))


def downgrade():
    pass
