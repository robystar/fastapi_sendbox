"""tabelle

Revision ID: 7a9c7d7e17f1
Revises: 56413fb0c716
Create Date: 2022-11-08 14:44:27.031699

"""
from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils
import sqlmodel # added
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '7a9c7d7e17f1'
down_revision = '56413fb0c716'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('ubicazione', schema='edilizia')
    op.alter_column('civico', 'civico',
               existing_type=sa.VARCHAR(),
               nullable=False,
               schema='edilizia')
    op.alter_column('posizione', 'istanza_id',
               existing_type=sa.INTEGER(),
               nullable=False,
               schema='edilizia')
    op.add_column('uiu', sa.Column('via_id', sa.Integer(), nullable=False), schema='edilizia')
    op.alter_column('uiu', 'civico',
               existing_type=sa.VARCHAR(),
               nullable=False,
               schema='edilizia')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('uiu', 'civico',
               existing_type=sa.VARCHAR(),
               nullable=True,
               schema='edilizia')
    op.drop_column('uiu', 'via_id', schema='edilizia')
    op.alter_column('posizione', 'istanza_id',
               existing_type=sa.INTEGER(),
               nullable=True,
               schema='edilizia')
    op.alter_column('civico', 'civico',
               existing_type=sa.VARCHAR(),
               nullable=True,
               schema='edilizia')
    op.create_table('ubicazione',
    sa.Column('localita', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('note', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('coord_lng', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('coord_lat', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('coord_x', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('coord_y', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('id', sa.INTEGER(), server_default=sa.text("nextval('edilizia.ubicazione_id_seq'::regclass)"), autoincrement=True, nullable=False),
    sa.Column('istanza_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['istanza_id'], ['edilizia.istanza.id'], name='ubicazione_istanza_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='ubicazione_pkey'),
    schema='edilizia'
    )
    # ### end Alembic commands ###
