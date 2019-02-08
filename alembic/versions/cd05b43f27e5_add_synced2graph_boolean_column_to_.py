"""Add synced2graph boolean column to version table.

Revision ID: cd05b43f27e5
Revises: 49fb7de6227f
Create Date: 2018-01-15 10:51:58.966052

"""

# revision identifiers, used by Alembic.
revision = 'cd05b43f27e5'
down_revision = '49fb7de6227f'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    """Upgrade the database to a newer revision."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        'versions',
        sa.Column('synced2graph', sa.Boolean(), server_default='FALSE', nullable=False))
    # ### end Alembic commands ###


def downgrade():
    """Downgrade the database to an older revision."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('versions', 'synced2graph')
    # ### end Alembic commands ###
