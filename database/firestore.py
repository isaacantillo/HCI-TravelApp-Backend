from google.cloud import firestore
from typing import List, Dict, Any, Optional
from dotenv import load_dotenv
import os

load_dotenv()

# Initialize Firestore client
db = firestore.Client(project=os.getenv("GOOGLE_APPLICATION_PROJECT_ID"))

class DatabaseManager:
    def __init__(self):
        self.db = db

    # Generic CRUD operations
    async def create_document(self, collection: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """Create a new document in the specified collection."""
        doc_ref = self.db.collection(collection).document()
        doc_ref.set(data)
        return {"id": doc_ref.id, **data}

    async def get_document(self, collection: str, doc_id: str) -> Optional[Dict[str, Any]]:
        """Get a document by ID from the specified collection."""
        doc_ref = self.db.collection(collection).document(doc_id)
        doc = doc_ref.get()
        if doc.exists:
            return {"id": doc.id, **doc.to_dict()}
        return None

    async def get_all_documents(self, collection: str) -> List[Dict[str, Any]]:
        """Get all documents from the specified collection."""
        docs = self.db.collection(collection).stream()
        return [{"id": doc.id, **doc.to_dict()} for doc in docs]

    async def update_document(self, collection: str, doc_id: str, data: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """Update a document in the specified collection."""
        doc_ref = self.db.collection(collection).document(doc_id)
        doc = doc_ref.get()
        if doc.exists:
            doc_ref.update(data)
            return {"id": doc_id, **data}
        return None

    async def delete_document(self, collection: str, doc_id: str) -> bool:
        """Delete a document from the specified collection."""
        doc_ref = self.db.collection(collection).document(doc_id)
        doc = doc_ref.get()
        if doc.exists:
            doc_ref.delete()
            return True
        return False

    # Specific collection operations
    async def create_user(self, user_data: Dict[str, Any]) -> Dict[str, Any]:
        """Create a new user."""
        return await self.create_document("users", user_data)

    async def get_user(self, user_id: str) -> Optional[Dict[str, Any]]:
        """Get a user by ID."""
        return await self.get_document("users", user_id)

    async def get_all_users(self) -> List[Dict[str, Any]]:
        """Get all users."""
        return await self.get_all_documents("users")

    async def update_user(self, user_id: str, user_data: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """Update a user."""
        return await self.update_document("users", user_id, user_data)

    async def delete_user(self, user_id: str) -> bool:
        """Delete a user."""
        return await self.delete_document("users", user_id)

    async def create_route(self, route_data: Dict[str, Any]) -> Dict[str, Any]:
        """Create a new route."""
        return await self.create_document("routes", route_data)

    async def get_route(self, route_id: str) -> Optional[Dict[str, Any]]:
        """Get a route by ID."""
        return await self.get_document("routes", route_id)

    async def get_all_routes(self) -> List[Dict[str, Any]]:
        """Get all routes."""
        return await self.get_all_documents("routes")

    async def update_route(self, route_id: str, route_data: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """Update a route."""
        return await self.update_document("routes", route_id, route_data)

    async def delete_route(self, route_id: str) -> bool:
        """Delete a route."""
        return await self.delete_document("routes", route_id)

    async def create_comment(self, comment_data: Dict[str, Any]) -> Dict[str, Any]:
        """Create a new comment."""
        return await self.create_document("comments", comment_data)

    async def get_comment(self, comment_id: str) -> Optional[Dict[str, Any]]:
        """Get a comment by ID."""
        return await self.get_document("comments", comment_id)

    async def get_all_comments(self) -> List[Dict[str, Any]]:
        """Get all comments."""
        return await self.get_all_documents("comments")

    async def update_comment(self, comment_id: str, comment_data: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """Update a comment."""
        return await self.update_document("comments", comment_id, comment_data)

    async def delete_comment(self, comment_id: str) -> bool:
        """Delete a comment."""
        return await self.delete_document("comments", comment_id)

# Create a singleton instance
firestore_manager = DatabaseManager()