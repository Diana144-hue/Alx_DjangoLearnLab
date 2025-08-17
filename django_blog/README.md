🔹 Blog Post Management Overview

ListView (/) – shows all blog posts.

DetailView (/posts/<pk>/) – shows post details.

CreateView (/posts/new/) – allows logged-in users to create posts.

UpdateView (/posts/<pk>/edit/) – allows post authors to edit.

DeleteView (/posts/<pk>/delete/) – allows authors to delete.

🔹 Developer Notes

Uses Django's class-based views for simplicity and reusability.

Uses LoginRequiredMixin and UserPassesTestMixin for access control.

Author is automatically set based on logged-in user.

published_date is set via auto_now_add.