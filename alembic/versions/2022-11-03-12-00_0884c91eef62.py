"""tabelle

Revision ID: 0884c91eef62
Revises: 9089dc1ef2f7
Create Date: 2022-11-03 12:00:41.182163

"""
from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils
import sqlmodel # added


# revision identifiers, used by Alembic.
revision = '0884c91eef62'
down_revision = '9089dc1ef2f7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('ingredient',
    sa.Column('name', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('amount', sa.Float(), nullable=False),
    sa.Column('id', sqlmodel.sql.sqltypes.GUID(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    schema='ricette'
    )
    op.create_index(op.f('ix_ricette_ingredient_id'), 'ingredient', ['id'], unique=False, schema='ricette')
    op.create_table('recipe',
    sa.Column('name', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('description', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('imagePath', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('id', sqlmodel.sql.sqltypes.GUID(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    schema='ricette'
    )
    op.create_index(op.f('ix_ricette_recipe_id'), 'recipe', ['id'], unique=False, schema='ricette')
    op.create_table('linkrecipeingredient',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('recipe_id', sqlmodel.sql.sqltypes.GUID(), nullable=False),
    sa.Column('ingredient_id', sqlmodel.sql.sqltypes.GUID(), nullable=False),
    sa.ForeignKeyConstraint(['ingredient_id'], ['ricette.ingredient.id'], ),
    sa.ForeignKeyConstraint(['recipe_id'], ['ricette.recipe.id'], ),
    sa.PrimaryKeyConstraint('id', 'recipe_id', 'ingredient_id'),
    schema='ricette'
    )
    op.create_index(op.f('ix_ricette_linkrecipeingredient_id'), 'linkrecipeingredient', ['id'], unique=False, schema='ricette')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_ricette_linkrecipeingredient_id'), table_name='linkrecipeingredient', schema='ricette')
    op.drop_table('linkrecipeingredient', schema='ricette')
    op.drop_index(op.f('ix_ricette_recipe_id'), table_name='recipe', schema='ricette')
    op.drop_table('recipe', schema='ricette')
    op.drop_index(op.f('ix_ricette_ingredient_id'), table_name='ingredient', schema='ricette')
    op.drop_table('ingredient', schema='ricette')
    # ### end Alembic commands ###
