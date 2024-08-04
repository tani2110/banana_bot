import React from "react";
import { Link } from "react-router-dom";
import "./sell.css";
import Item from "../components/Item";

const Sell = () => {
  const breakPoints = [
    { width: 1, itemsToShow: 1 },
    { width: 550, itemsToShow: 2 },
    { width: 768, itemsToShow: 3 },
  ];

  const products = [
    {
      id: "6499fb2c19a955784d4d024e",
      imag: "https://m.media-amazon.com/images/I/51YlmV6WspL._AC_UL400_.jpg",
      text: "Face Wash",
      price: 150,
    },
    {
      id: "6499f91d19a955784d4d0247",
      imag: "https://m.media-amazon.com/images/I/71LFp0q3PdL._AC_UL400_.jpg",
      text: "Parachute Men Hair Gel",
      price: 300,
    },
  ];
  return (
    <div>
      <div className="prev-next">
        <div className="left">
          <Link to="/">Home</Link>
        </div>
      </div>

      <div className="main-content">
        <div className="sellcarou">
          {/* <Carousel breakPoints={breakPoints} pagination={false}> */}
          {products.map((product) => (
            <Link to={`/products/id/${product.id}`}>
              <Item
                imag={product.imag}
                text={product.text}
                price={product.price}
              ></Item>
            </Link>
          ))}
          {/* </Carousel> */}
        </div>

        <div className="product-image">
          <img
            src={require("../images/ramdomDSLR.jpg")}
            id="display-image"
            alt="DSLR"
          ></img>
        </div>
        <div className="product-buy">
          <h1>Product Name:</h1>
          <p id="product-id">ID: </p>
          <br />

          <table cellSpacing="20px">
            <tr>
              <td>
                <p id="price-display"> Minimum Bid:</p>
              </td>
              <td>
                {" "}
                <p id="price-display">&#8377;420</p>
              </td>
              <button type="button" id="edit">
                {" "}
                EDIT{" "}
              </button>
            </tr>
            <tr>
              <td>
                <p id="price-display">Bid End Date: </p>
              </td>

              <td>
                {" "}
                <p id="price-display">69/6/9</p>
              </td>
              <button type="button" id="edit">
                EDIT
              </button>
            </tr>
          </table>

          <Link to="/new">
            <button type="button" id="btn-new">
              Add New +
            </button>
          </Link>
          <button type="button" id="btn-cartt">
            Freeze
          </button>
        </div>
      </div>
    </div>
  );
};

export default Sell;
