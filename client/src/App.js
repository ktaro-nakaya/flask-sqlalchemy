import logo from './logo.svg';
import './App.css';
import React, {useState} from "react"

function App() {

  const [itemList, setItemList] = useState([])

  function getData(e){
    fetch("/api/alchemy/")
    .then(response => response.json())
    .then(json => setItemList(json))
  }

  return (
    <div className="App">
      {
        itemList.length ?(
          itemList.map( item =>{
            return(
              <div key={item.id}>
                <h3>id:{item.id}</h3>
                <h3>name:{item.name}</h3>
                <h3>price:{item.price}</h3>
              </div>
            )
          }
        )
        ):(
          <div>
            <h1>データがない</h1>
            <button onClick={()=>getData()} >データ取得</button>
          </div>)
        }
        
    </div>
  );
}

export default App;
