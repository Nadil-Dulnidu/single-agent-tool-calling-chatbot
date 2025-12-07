from pydantic import BaseModel, Field

class Article(BaseModel):
    title: str = Field(..., description="The title of the article")
    source: str = Field(..., description="The source of the article")
    link: str = Field(..., description="The URL link to the article")
    snippet: str = Field(..., description="A brief snippet or summary of the article")

    @classmethod
    def from_serpapi_result(cls, result: dict) -> "Article":
        return cls(
            title=result["title"],
            source=result["source"],
            link=result["link"],
            snippet=result["snippet"],
        )