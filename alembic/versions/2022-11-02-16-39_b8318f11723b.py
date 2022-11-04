"""tabelle

Revision ID: b8318f11723b
Revises: 
Create Date: 2022-11-02 16:39:07.213538

"""
from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils
import sqlmodel # added


# revision identifiers, used by Alembic.
revision = 'b8318f11723b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('role',
    sa.Column('name', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('description', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('id', sqlmodel.sql.sqltypes.GUID(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    schema='admin'
    )
    op.create_index(op.f('ix_admin_role_id'), 'role', ['id'], unique=False, schema='admin')
    op.create_table('richiedente',
    sa.Column('piva', sa.String(length=11), nullable=True),
    sa.Column('codcat_nato', sa.String(length=4), nullable=True),
    sa.Column('cf', sa.String(length=16), nullable=True),
    sa.Column('email', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('pec', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('telefono', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('cellulare', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('fax', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('comune', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('prov', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('loc', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('cap', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('indirizzo', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('civico', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('app', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('nome', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('cognome', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('data_nato', sa.Date(), nullable=True),
    sa.Column('comune_nato', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('prov_nato', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('loc_nato', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('cittadinanza', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('sesso', sa.Enum('M', 'F', name='sessotype'), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    schema='edilizia'
    )
    op.create_table('user',
    sa.Column('birthdate', sa.DateTime(timezone=True), nullable=True),
    sa.Column('first_name', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('last_name', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('email', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('is_active', sa.Boolean(), nullable=False),
    sa.Column('is_superuser', sa.Boolean(), nullable=False),
    sa.Column('phone', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('state', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('country', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('address', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('id', sqlmodel.sql.sqltypes.GUID(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('hashed_password', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('role_id', sqlmodel.sql.sqltypes.GUID(), nullable=True),
    sa.ForeignKeyConstraint(['role_id'], ['admin.role.id'], ),
    sa.PrimaryKeyConstraint('id'),
    schema='admin'
    )
    op.create_index(op.f('ix_admin_user_email'), 'user', ['email'], unique=True, schema='admin')
    op.create_index(op.f('ix_admin_user_hashed_password'), 'user', ['hashed_password'], unique=False, schema='admin')
    op.create_index(op.f('ix_admin_user_id'), 'user', ['id'], unique=False, schema='admin')
    op.create_table('group',
    sa.Column('name', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('description', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('id', sqlmodel.sql.sqltypes.GUID(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('created_by_id', sqlmodel.sql.sqltypes.GUID(), nullable=True),
    sa.ForeignKeyConstraint(['created_by_id'], ['admin.user.id'], ),
    sa.PrimaryKeyConstraint('id'),
    schema='admin'
    )
    op.create_index(op.f('ix_admin_group_id'), 'group', ['id'], unique=False, schema='admin')
    op.create_table('istanza',
    sa.Column('data_presentazione', sa.DateTime(), nullable=True),
    sa.Column('tipo', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('sportello', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('oggetto', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('intervento', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('note', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('created_by_id', sqlmodel.sql.sqltypes.GUID(), nullable=True),
    sa.ForeignKeyConstraint(['created_by_id'], ['admin.user.id'], ),
    sa.PrimaryKeyConstraint('id'),
    schema='edilizia'
    )
    op.create_index(op.f('ix_edilizia_istanza_id'), 'istanza', ['id'], unique=False, schema='edilizia')
    op.create_table('pratica',
    sa.Column('numero_pratica', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('data_presentazione', sa.DateTime(), nullable=True),
    sa.Column('tipo_pratica', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('anno_pratica', sa.Integer(), nullable=True),
    sa.Column('tipo_intervento', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('tipo_procedimento', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('oggetto', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('intervento', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('note', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('created_by_id', sqlmodel.sql.sqltypes.GUID(), nullable=True),
    sa.ForeignKeyConstraint(['created_by_id'], ['admin.user.id'], ),
    sa.PrimaryKeyConstraint('id'),
    schema='edilizia'
    )
    op.create_index(op.f('ix_edilizia_pratica_id'), 'pratica', ['id'], unique=False, schema='edilizia')
    op.create_table('linkgroupuser',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('group_id', sqlmodel.sql.sqltypes.GUID(), nullable=False),
    sa.Column('user_id', sqlmodel.sql.sqltypes.GUID(), nullable=False),
    sa.ForeignKeyConstraint(['group_id'], ['admin.group.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['admin.user.id'], ),
    sa.PrimaryKeyConstraint('id', 'group_id', 'user_id'),
    schema='admin'
    )
    op.create_index(op.f('ix_admin_linkgroupuser_id'), 'linkgroupuser', ['id'], unique=False, schema='admin')
    op.create_table('linkistanzapratica',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('istanza_id', sa.Integer(), nullable=False),
    sa.Column('pratica_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['istanza_id'], ['edilizia.istanza.id'], ),
    sa.ForeignKeyConstraint(['pratica_id'], ['edilizia.pratica.id'], ),
    sa.PrimaryKeyConstraint('id', 'istanza_id', 'pratica_id'),
    schema='edilizia'
    )
    op.create_index(op.f('ix_edilizia_linkistanzapratica_id'), 'linkistanzapratica', ['id'], unique=False, schema='edilizia')
    op.create_table('linkistanzauser',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('istanza_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sqlmodel.sql.sqltypes.GUID(), nullable=False),
    sa.ForeignKeyConstraint(['istanza_id'], ['edilizia.istanza.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['admin.user.id'], ),
    sa.PrimaryKeyConstraint('id', 'istanza_id', 'user_id'),
    schema='edilizia'
    )
    op.create_index(op.f('ix_edilizia_linkistanzauser_id'), 'linkistanzauser', ['id'], unique=False, schema='edilizia')
    op.create_table('linkpraticauser',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('pratica_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sqlmodel.sql.sqltypes.GUID(), nullable=False),
    sa.ForeignKeyConstraint(['pratica_id'], ['edilizia.pratica.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['admin.user.id'], ),
    sa.PrimaryKeyConstraint('id', 'pratica_id', 'user_id'),
    schema='edilizia'
    )
    op.create_index(op.f('ix_edilizia_linkpraticauser_id'), 'linkpraticauser', ['id'], unique=False, schema='edilizia')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_edilizia_linkpraticauser_id'), table_name='linkpraticauser', schema='edilizia')
    op.drop_table('linkpraticauser', schema='edilizia')
    op.drop_index(op.f('ix_edilizia_linkistanzauser_id'), table_name='linkistanzauser', schema='edilizia')
    op.drop_table('linkistanzauser', schema='edilizia')
    op.drop_index(op.f('ix_edilizia_linkistanzapratica_id'), table_name='linkistanzapratica', schema='edilizia')
    op.drop_table('linkistanzapratica', schema='edilizia')
    op.drop_index(op.f('ix_admin_linkgroupuser_id'), table_name='linkgroupuser', schema='admin')
    op.drop_table('linkgroupuser', schema='admin')
    op.drop_index(op.f('ix_edilizia_pratica_id'), table_name='pratica', schema='edilizia')
    op.drop_table('pratica', schema='edilizia')
    op.drop_index(op.f('ix_edilizia_istanza_id'), table_name='istanza', schema='edilizia')
    op.drop_table('istanza', schema='edilizia')
    op.drop_index(op.f('ix_admin_group_id'), table_name='group', schema='admin')
    op.drop_table('group', schema='admin')
    op.drop_index(op.f('ix_admin_user_id'), table_name='user', schema='admin')
    op.drop_index(op.f('ix_admin_user_hashed_password'), table_name='user', schema='admin')
    op.drop_index(op.f('ix_admin_user_email'), table_name='user', schema='admin')
    op.drop_table('user', schema='admin')
    op.drop_table('richiedente', schema='edilizia')
    op.drop_index(op.f('ix_admin_role_id'), table_name='role', schema='admin')
    op.drop_table('role', schema='admin')
    # ### end Alembic commands ###