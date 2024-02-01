"""add contant column to newpost table

Revision ID: 650eb7b6ce8d
Revises: 3da014a7f461
Create Date: 2024-01-31 14:58:09.907214

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '650eb7b6ce8d'
down_revision: Union[str, None] = '3da014a7f461'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('newposts',sa.Column('content',sa.String(),nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('newposts','content')
    pass
