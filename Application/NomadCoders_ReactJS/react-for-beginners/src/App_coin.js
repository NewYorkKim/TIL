import { useEffect, useState } from "react";

function App() {
    const [loading, setLoading] = useState(true);
    const [coins, setCoins] = useState([]);
    const [result, setResult] = useState(true);
    const [money, setMoney] = useState();
    const [selected, setSelected] = useState("");
    const [calculate, setCalculate] = useState(true);
    const [amount, setAmount] = useState("");
    useEffect(() => {
        fetch("https://api.coinpaprika.com/v1/tickers")
        .then(response => response.json())
        .then((json) => {
            setCoins(json);
            setLoading(false);
        });
    }, []);
    const onSubmit = (event) => {
        event.preventDefault();
        if (money === "") {
            return;
        }
        setMoney(current => current);
        setResult(false);
    }
    const handleMoney = (event) => setMoney(event.target.value);
    const handleSelected = (event) => setSelected(event.target.value);
    const onClick = () => {
        setCalculate(false);
        console.log(money);
        if (money === 0 | money === "") {
            setAmount("nothing");
        }
        setAmount(parseInt(money / selected.split(" ")[2]) > 0 ? parseInt(money / selected.split(" ")[2]) : "nothing");
    }
    return (
    <div>
        <h1>The Coins! ({coins.length})</h1>
        {loading ? <strong>Loading...</strong> : 
        <div>
            <select onChange={handleSelected} value={selected}>
                {coins.map((coin) => <option key={coin.id}>{coin.name} ({coin.symbol}): {coin.quotes.USD.price} USD</option>)}
            </select>
            <form onSubmit={onSubmit}>
                <input onChange={handleMoney} type="int" placeholder="Your money" />
                <button>Submit</button>
            </form>
            <br/>
            {result ? null : 
            <div id="result">
                Your money: {money} USD
                <br/>
                Your coin: {selected.split(" ")[0]}
                <br/><br/>
                <button onClick={onClick}>Calculate</button>
                <br/><br/>
                {calculate ? null : 
                <strong>You can buy {amount} {selected.split(" ")[0]}</strong>
                }
            </div>
            }
        </div>
        }
    </div>
    );
}

export default App;