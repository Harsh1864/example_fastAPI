"""add last few columns to newpost

Revision ID: 0bcf4e514f0f
Revises: 123a7887e4e5
Create Date: 2024-01-31 18:18:34.625739

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0bcf4e514f0f'
down_revision: Union[str, None] = '123a7887e4e5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('newposts',sa.Column(
        'published',sa.Boolean(),nullable=False,server_default='True'),)
    op.add_column('newposts',sa.Column(
        'created_at',sa.TIMESTAMP(timezone=True),nullable=False,server_default=sa.text('NOW()')),)
    pass


def downgrade() -> None:
    op.drop_column('newposts','published')
    op.drop_column('newposts','created_at')
    
    pass
