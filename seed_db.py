import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ebooks_project.settings')
django.setup()

from store.models import Category, Author, Book

def seed():
    print("Seeding database with authentic real-world books and authors...")

    # Clear existing data
    Book.objects.all().delete()
    Author.objects.all().delete()
    Category.objects.all().delete()

    # Categories
    cat_fiction = Category.objects.create(name="Fiction & Literature", slug="fiction", description="Classic and modern fictional literature.")
    cat_scifi = Category.objects.create(name="Science Fiction", slug="sci-fi", description="Futuristic science fiction and space epics.")
    cat_fantasy = Category.objects.create(name="Fantasy", slug="fantasy", description="Magical realms, mythical creatures, and epic adventures.")
    cat_tech = Category.objects.create(name="Technology & Software", slug="technology", description="Programming, system design, and software engineering.")
    cat_business = Category.objects.create(name="Business & Finance", slug="business", description="Entrepreneurship, investing, and economics.")
    cat_selfhelp = Category.objects.create(name="Personal Growth", slug="personal-growth", description="Productivity, habits, and self-improvement.")

    # Real Authors
    a_fitzgerald = Author.objects.create(
        name="F. Scott Fitzgerald",
        genre="Classic Fiction",
        bio="American novelist widely regarded as one of the greatest writers of the 20th century, famous for depicting the Jazz Age.",
        image="https://images.unsplash.com/photo-1534528741775-53994a69daeb?auto=format&fit=crop&w=400&q=80",
        books_count=12
    )

    a_orwell = Author.objects.create(
        name="George Orwell",
        genre="Dystopian Fiction",
        bio="English novelist, journalist, and social critic world-famous for 1984 and Animal Farm.",
        image="https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?auto=format&fit=crop&w=400&q=80",
        books_count=8
    )

    a_harper = Author.objects.create(
        name="Harper Lee",
        genre="Classic Literature",
        bio="Pulitzer Prize-winning American novelist best known for To Kill a Mockingbird.",
        image="https://images.unsplash.com/photo-1544005313-94ddf0286df2?auto=format&fit=crop&w=400&q=80",
        books_count=4
    )

    a_herbert = Author.objects.create(
        name="Frank Herbert",
        genre="Science Fiction",
        bio="Acclaimed sci-fi author best known for his 1965 masterpiece Dune, winner of Hugo and Nebula awards.",
        image="https://images.unsplash.com/photo-1500648767791-00dcc994a43e?auto=format&fit=crop&w=400&q=80",
        books_count=15
    )

    a_tolkien = Author.objects.create(
        name="J.R.R. Tolkien",
        genre="High Fantasy",
        bio="English scholar, philologist, and university professor best known for The Hobbit and The Lord of the Rings.",
        image="https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?auto=format&fit=crop&w=400&q=80",
        books_count=20
    )

    a_asimov = Author.objects.create(
        name="Isaac Asimov",
        genre="Science Fiction",
        bio="Prolific science fiction writer and biochemistry professor famous for the Foundation series and Three Laws of Robotics.",
        image="https://images.unsplash.com/photo-1506794778202-cad84cf45f1d?auto=format&fit=crop&w=400&q=80",
        books_count=40
    )

    a_martin = Author.objects.create(
        name="Robert C. Martin",
        genre="Software Engineering",
        bio="Software engineer, international speaker, and author known as 'Uncle Bob', co-author of the Agile Manifesto.",
        image="https://images.unsplash.com/photo-1519085360753-af0119f7cbe7?auto=format&fit=crop&w=400&q=80",
        books_count=10
    )

    a_kleppmann = Author.objects.create(
        name="Martin Kleppmann",
        genre="Distributed Systems",
        bio="Researcher in distributed systems at the University of Cambridge and author of Designing Data-Intensive Applications.",
        image="https://images.unsplash.com/photo-1522075469751-3a6694fb2f61?auto=format&fit=crop&w=400&q=80",
        books_count=5
    )

    a_clear = Author.objects.create(
        name="James Clear",
        genre="Personal Development",
        bio="Author and speaker focused on habits, decision-making, and continuous self-improvement.",
        image="https://images.unsplash.com/photo-1500648767791-00dcc994a43e?auto=format&fit=crop&w=400&q=80",
        books_count=3
    )

    a_kahneman = Author.objects.create(
        name="Daniel Kahneman",
        genre="Behavioral Economics",
        bio="Nobel Memorial Prize winner in Economic Sciences famous for his groundbreaking research in decision-making psychology.",
        image="https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?auto=format&fit=crop&w=400&q=80",
        books_count=6
    )

    a_kiyosaki = Author.objects.create(
        name="Robert T. Kiyosaki",
        genre="Personal Finance",
        bio="American businessman, founder of Rich Global LLC, and author of the world's #1 personal finance book Rich Dad Poor Dad.",
        image="https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?auto=format&fit=crop&w=400&q=80",
        books_count=18
    )

    a_ries = Author.objects.create(
        name="Eric Ries",
        genre="Entrepreneurship",
        bio="Silicon Valley entrepreneur, blogger, and author of The Lean Startup, pioneering lean methodologies.",
        image="https://images.unsplash.com/photo-1534528741775-53994a69daeb?auto=format&fit=crop&w=400&q=80",
        books_count=4
    )

    # Real Books Data
    books_data = [
        # Fiction & Classics
        {
            "title": "The Great Gatsby",
            "author": a_fitzgerald,
            "category": cat_fiction,
            "price": 12.99,
            "rating": 4.8,
            "reviews_count": 2450,
            "description": "Set in the summer of 1922 on Long Island, F. Scott Fitzgerald's classic explores themes of idealism, resistance to change, social upheaval, and excess in the Roaring Twenties.",
            "image": "https://images.unsplash.com/photo-1544716278-ca5e3f4abd8c?auto=format&fit=crop&w=600&q=80",
            "is_featured": True
        },
        {
            "title": "To Kill a Mockingbird",
            "author": a_harper,
            "category": cat_fiction,
            "price": 14.99,
            "rating": 4.9,
            "reviews_count": 3120,
            "description": "Harper Lee's Pulitzer Prize-winning masterpiece of honor and injustice in the Deep South, viewed through the eyes of young Scout Finch as her father defends a wrongly accused man.",
            "image": "https://images.unsplash.com/photo-1543002588-bfa74002ed7e?auto=format&fit=crop&w=600&q=80",
            "is_featured": True
        },
        {
            "title": "1984",
            "author": a_orwell,
            "category": cat_fiction,
            "price": 13.50,
            "rating": 4.9,
            "reviews_count": 4890,
            "description": "Winston Smith rewrites history for the Ministry of Truth in a totalitarian world ruled by Big Brother. George Orwell's prophetic vision remains the ultimate warning on surveillance.",
            "image": "https://images.unsplash.com/photo-1512820790803-83ca734da794?auto=format&fit=crop&w=600&q=80",
            "is_featured": True
        },
        {
            "title": "Animal Farm",
            "author": a_orwell,
            "category": cat_fiction,
            "price": 9.99,
            "rating": 4.7,
            "reviews_count": 1820,
            "description": "A farm is taken over by its overworked, mistreated animals. Intending to create a paradise of progress and equality, a tyrannical pig named Napoleon leads them into totalitarian rule.",
            "image": "https://images.unsplash.com/photo-1497633762265-9d179a990aa6?auto=format&fit=crop&w=600&q=80",
            "is_featured": False
        },

        # Sci-Fi & Fantasy
        {
            "title": "Dune",
            "author": a_herbert,
            "category": cat_scifi,
            "price": 18.99,
            "rating": 4.9,
            "reviews_count": 3890,
            "description": "Set on the desert planet Arrakis, Dune tells the story of Paul Atreides as he navigates political intrigue, religious prophecy, and the battle for the universe's most vital resource: spice.",
            "image": "https://images.unsplash.com/photo-1532012197267-da84d127e765?auto=format&fit=crop&w=600&q=80",
            "is_featured": True
        },
        {
            "title": "The Hobbit",
            "author": a_tolkien,
            "category": cat_fantasy,
            "price": 16.80,
            "rating": 4.9,
            "reviews_count": 5200,
            "description": "Bilbo Baggins is a comfortable, unambitious hobbit whose quiet life is disrupted when the wizard Gandalf and thirteen dwarves hire him as a burglar to reclaim Smaug's treasure.",
            "image": "https://images.unsplash.com/photo-1495640388908-05fa85288e61?auto=format&fit=crop&w=600&q=80",
            "is_featured": True
        },
        {
            "title": "Foundation",
            "author": a_asimov,
            "category": cat_scifi,
            "price": 15.50,
            "rating": 4.8,
            "reviews_count": 2100,
            "description": "Psychohistorian Hari Seldon foresees the fall of the Galactic Empire and creates the Foundation to preserve human knowledge across thousands of years of dark ages.",
            "image": "https://images.unsplash.com/photo-1451187580459-43490279c0fa?auto=format&fit=crop&w=600&q=80",
            "is_featured": False
        },

        # Technology & Software
        {
            "title": "Clean Code: Agile Software Craftsmanship",
            "author": a_martin,
            "category": cat_tech,
            "price": 34.99,
            "rating": 4.8,
            "reviews_count": 1450,
            "description": "Even bad code can function. But if code isn't clean, it can bring a development organization to its knees. Uncle Bob presents revolutionary principles for writing maintainable code.",
            "image": "https://images.unsplash.com/photo-1555066931-4365d14bab8c?auto=format&fit=crop&w=600&q=80",
            "is_featured": True
        },
        {
            "title": "Designing Data-Intensive Applications",
            "author": a_kleppmann,
            "category": cat_tech,
            "price": 44.99,
            "rating": 4.95,
            "reviews_count": 2300,
            "description": "An invaluable deep dive into the architecture of databases, distributed systems, consensus algorithms, streaming pipelines, and fault-tolerant cloud applications.",
            "image": "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?auto=format&fit=crop&w=600&q=80",
            "is_featured": True
        },
        {
            "title": "Clean Architecture",
            "author": a_martin,
            "category": cat_tech,
            "price": 32.50,
            "rating": 4.75,
            "reviews_count": 980,
            "description": "Practical software architecture solutions from Robert C. Martin on component design, solid principles, separation of concerns, and system structure.",
            "image": "https://images.unsplash.com/photo-1517694712202-14dd9538aa97?auto=format&fit=crop&w=600&q=80",
            "is_featured": False
        },

        # Business & Self Improvement
        {
            "title": "Atomic Habits",
            "author": a_clear,
            "category": cat_selfhelp,
            "price": 17.99,
            "rating": 4.95,
            "reviews_count": 6800,
            "description": "No matter your goals, Atomic Habits offers a proven framework for improving every day. James Clear reveals practical strategies for building good habits and breaking bad ones.",
            "image": "https://images.unsplash.com/photo-1499750310107-5fef28a66643?auto=format&fit=crop&w=600&q=80",
            "is_featured": True
        },
        {
            "title": "Thinking, Fast and Slow",
            "author": a_kahneman,
            "category": cat_business,
            "price": 16.50,
            "rating": 4.8,
            "reviews_count": 3400,
            "description": "Nobel laureate Daniel Kahneman takes us on a groundbreaking tour of the mind, explaining the two systems that drive the way we think: System 1 (fast, emotional) and System 2 (slow, logical).",
            "image": "https://images.unsplash.com/photo-1456513080510-7bf3a84b82f8?auto=format&fit=crop&w=600&q=80",
            "is_featured": True
        },
        {
            "title": "Rich Dad Poor Dad",
            "author": a_kiyosaki,
            "category": cat_business,
            "price": 15.00,
            "rating": 4.7,
            "reviews_count": 5100,
            "description": "Robert Kiyosaki's story of growing up with two dads—his real father and his best friend's rich dad—and the ways in which both men shaped his thoughts about money and investing.",
            "image": "https://images.unsplash.com/photo-1553729459-efe14ef6055d?auto=format&fit=crop&w=600&q=80",
            "is_featured": False
        },
        {
            "title": "The Lean Startup",
            "author": a_ries,
            "category": cat_business,
            "price": 21.99,
            "rating": 4.85,
            "reviews_count": 2750,
            "description": "Most startups fail. But many of those failures are preventable. The Lean Startup is a new approach being adopted across the globe to change how companies are built and products launched.",
            "image": "https://images.unsplash.com/photo-1519389950473-47ba0277781c?auto=format&fit=crop&w=600&q=80",
            "is_featured": True
        }
    ]

    for b in books_data:
        Book.objects.create(**b)

    print(f"Successfully seeded {Category.objects.count()} categories, {Author.objects.count()} authors, and {Book.objects.count()} real best-selling books into SQLite database!")

if __name__ == '__main__':
    seed()
