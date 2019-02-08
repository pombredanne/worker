"""Drop tables esmarker, similar_stacks, similar_components, and stacks.

Revision ID: ddb09a7d6633
Revises: 750621a9cd89
Create Date: 2017-04-06 12:32:34.124884

"""

# revision identifiers, used by Alembic.
revision = 'ddb09a7d6633'
down_revision = '750621a9cd89'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql


def upgrade():
    """Upgrade the database to a newer revision."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('esmarker')
    op.drop_table('similar_stacks')
    op.drop_table('similar_components')
    op.drop_table('stacks')
    # ### end Alembic commands ###


def downgrade():
    """Downgrade the database to an older revision."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('stacks',
                    sa.Column('id', sa.INTEGER(),
                              server_default=sa.text("nextval('stacks_id_seq'::regclass)"),
                              nullable=False),
                    sa.Column('is_ref_stack', sa.BOOLEAN(), autoincrement=False, nullable=False),
                    sa.Column('stack_json', postgresql.JSONB(astext_type=sa.Text()),
                              autoincrement=False, nullable=False),
                    sa.PrimaryKeyConstraint('id', name='stacks_pkey'),
                    postgresql_ignore_search_path=False)
    op.create_table('similar_components',
                    sa.Column('id', sa.INTEGER(), nullable=False),
                    sa.Column('fromcomponent', sa.TEXT(), autoincrement=False, nullable=False),
                    sa.Column('tocomponent', sa.TEXT(), autoincrement=False, nullable=False),
                    sa.Column('similarity_distance', postgresql.DOUBLE_PRECISION(precision=53),
                              autoincrement=False, nullable=False),
                    sa.PrimaryKeyConstraint('id', name='similar_components_pkey'),
                    sa.UniqueConstraint('fromcomponent', 'tocomponent', name='sim_comps'))
    op.create_table('similar_stacks',
                    sa.Column('id', sa.INTEGER(), nullable=False),
                    sa.Column('analysis', postgresql.JSONB(astext_type=sa.Text()),
                              autoincrement=False, nullable=True),
                    sa.Column('similar_stack_id', sa.INTEGER(), autoincrement=False,
                              nullable=False),
                    sa.Column('similarity_value', postgresql.DOUBLE_PRECISION(precision=53),
                              autoincrement=False, nullable=False),
                    sa.Column('stack_id', sa.INTEGER(), autoincrement=False, nullable=False),
                    sa.ForeignKeyConstraint(['similar_stack_id'], ['stacks.id'],
                                            name='similar_stacks_similar_stack_id_fkey'),
                    sa.ForeignKeyConstraint(['stack_id'], ['stacks.id'],
                                            name='similar_stacks_stack_id_fkey'),
                    sa.PrimaryKeyConstraint('id', name='similar_stacks_pkey'),
                    sa.UniqueConstraint('stack_id', 'similar_stack_id', name='sim_unique'))
    op.create_table('esmarker',
                    sa.Column('id', sa.INTEGER(), nullable=False),
                    sa.Column('worker_result_id', sa.INTEGER(), autoincrement=False,
                              nullable=True),
                    sa.ForeignKeyConstraint(['worker_result_id'], ['worker_results.id'],
                                            name='esmarker_worker_result_id_fkey'),
                    sa.PrimaryKeyConstraint('id', name='esmarker_pkey'))
    # ### end Alembic commands ###
