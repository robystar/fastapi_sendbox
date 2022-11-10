"""tabelle

Revision ID: c8883bcaac9e
Revises: 6d1bc12d31c8
Create Date: 2022-11-08 09:18:48.931094

"""
from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils
import sqlmodel # added
from geoalchemy2 import Geometry

# revision identifiers, used by Alembic.
revision = 'c8883bcaac9e'
down_revision = '6d1bc12d31c8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('via',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nome', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    schema='civici'
    )
    op.create_table('civico',
    sa.Column('geom_p', Geometry(geometry_type='POINT', srid=4326, from_text='ST_GeomFromEWKT', name='geometry'), nullable=True),
    sa.Column('civico', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('interno', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('note', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('istanza_id', sa.Integer(), nullable=False),
    sa.Column('via_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['istanza_id'], ['edilizia.istanza.id'], ),
    sa.ForeignKeyConstraint(['via_id'], ['civici.via.id'], ),
    sa.PrimaryKeyConstraint('id'),
    schema='edilizia'
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('vie',
    sa.Column('id', sa.INTEGER(), server_default=sa.text("nextval('civici.vie_id_seq'::regclass)"), autoincrement=True, nullable=False),
    sa.Column('specie', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('denominazione', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('orignome', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('nome', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('comune', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='vie_pkey'),
    schema='civici',
    comment='I campi via_lavagna e codice_lavagna riproducono i rispettivi nome e id della via nella tabella delle vie del programma di Pietro Vabai.'
    )
    op.drop_index('idx_civico_geom_p', table_name='civico', schema='edilizia', postgresql_using='gist')
    op.drop_table('civico', schema='edilizia')
    op.drop_table('via', schema='civici')
    # ### end Alembic commands ###