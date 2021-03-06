"""add table mailtemplates

Revision ID: 34f15d11d02
Revises: 2fadbf7a01a
Create Date: 2015-08-04 17:28:24.372803

"""

# revision identifiers, used by Alembic.
revision = '34f15d11d02'
down_revision = '2fadbf7a01a'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('mailtemplates',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=False),
    sa.Column('subject', sa.String(length=79), nullable=False),
    sa.Column('html', sa.Text(), nullable=False),
    sa.Column('help_msg', sa.Text(), nullable=True),
    sa.Column('updated_at', sa.Date(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('mailtemplates')
    ### end Alembic commands ###
