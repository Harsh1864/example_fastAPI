"""add foreign-key to newposts table

Revision ID: 123a7887e4e5
Revises: b0499ec4f141
Create Date: 2024-01-31 18:05:46.908223

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '123a7887e4e5'
down_revision: Union[str, None] = 'b0499ec4f141'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('newposts',sa.Column('owner_id',sa.Integer(),nullable=False))
    op.create_foreign_key('post_users_fk',source_table="newposts",referent_table="users",
                          local_cols=['owner_id'],remote_cols=['id'],ondelete="CASCADE")
    pass


def downgrade() -> None:
    op.drop_constraint('post_users_fk',table_name="newposts")
    op.drop_column('newposts','owner_id')
    pass
