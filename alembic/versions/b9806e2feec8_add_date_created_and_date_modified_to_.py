"""add date_created and date_modified to column to table anxieties

Revision ID: b9806e2feec8
Revises: 5816162c0fff
Create Date: 2020-03-23 18:11:14.601855

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b9806e2feec8'
down_revision = '5816162c0fff'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column(
    	"anxieties",
    	sa.Column("date_created", sa.types.DateTime))

    op.add_column(
    	"anxieties",
    	sa.Column("date_modified", sa.types.DateTime))

def downgrade():
    pass
