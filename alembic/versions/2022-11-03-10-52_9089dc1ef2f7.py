"""tabelle

Revision ID: 9089dc1ef2f7
Revises: c8c15321bb27
Create Date: 2022-11-03 10:52:56.051563

"""
from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils
import sqlmodel # added
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '9089dc1ef2f7'
down_revision = 'c8c15321bb27'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('domicilio',
    sa.Column('comune', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('prov', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('loc', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('cap', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('indirizzo', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('civico', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('richiedente_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['richiedente_id'], ['edilizia.richiedente.id'], ),
    sa.PrimaryKeyConstraint('id', 'richiedente_id'),
    schema='edilizia'
    )
    op.add_column('istanza', sa.Column('consenso_pec', sa.Boolean(), nullable=True), schema='edilizia')
    op.add_column('istanza', sa.Column('firma_digitale_opt', sa.Integer(), nullable=True), schema='edilizia')
    op.alter_column('istanza', 'data_presentazione',
               existing_type=postgresql.TIMESTAMP(),
               type_=sa.DateTime(timezone=True),
               existing_nullable=True,
               schema='edilizia')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('istanza', 'data_presentazione',
               existing_type=sa.DateTime(timezone=True),
               type_=postgresql.TIMESTAMP(),
               existing_nullable=True,
               schema='edilizia')
    op.drop_column('istanza', 'firma_digitale_opt', schema='edilizia')
    op.drop_column('istanza', 'consenso_pec', schema='edilizia')
    op.drop_table('domicilio', schema='edilizia')
    # ### end Alembic commands ###