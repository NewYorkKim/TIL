import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";

function Detail() {
    const { id } = useParams()
    const [loading, setLoading] = useState(true);
    const [detail, setDetail] = useState([]);
    const getMovie = async () => {
        const json = await (
            await fetch(
                `https://yts.mx/api/v2/movie_details.json?movie_id=${id}`
                )
        ).json();
        setDetail(json.data.movie);
        setLoading(false);
    }
    useEffect(() => {
        getMovie();
    }, []);
    return (
        <div>
            {loading ? (
                <h1>Laoding...</h1>
                ) : (
                    <div>
                        <img src={detail.medium_cover_image} alt={detail.title} />
                        <h1>{detail.title}</h1>
                        <ul>
                            <li>year: {detail.year}</li>
                            <li>rating: {detail.rating}</li>
                            <li>like count: {detail.like_count}</li>
                        </ul>
                        <p>{detail.description_full}</p>
                    </div>
            )}
        </div>
    );
}

export default Detail;