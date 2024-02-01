"""create posts table

Revision ID: 3da014a7f461
Revises: 
Create Date: 2024-01-31 13:21:22.623606

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3da014a7f461'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('newposts',sa.Column('id', sa.Integer(),nullable=False,primary_key=True),
                    sa.Column('title', sa.String(),nullable=False))
    pass


def downgrade() -> None:
    pass
