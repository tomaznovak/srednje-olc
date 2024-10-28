"""add content column to posts table

Revision ID: e96ca18edaac
Revises: f616e1f60475
Create Date: 2024-10-27 14:06:54.432908

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e96ca18edaac'
down_revision: Union[str, None] = 'f616e1f60475'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
