# Django Blog - CRUD Features

### Features:
- Users can create, read, update, and delete posts.
- Only authenticated users can create posts.
- Only post authors can edit or delete their own posts.
- Anyone (authenticated or not) can view posts.

### URLs:
- /posts/ → List all posts
- /posts/new/ → Create new post
- /posts/<id>/ → View post details
- /posts/<id>/edit/ → Edit post (author only)
- /posts/<id>/delete/ → Delete post (author only)