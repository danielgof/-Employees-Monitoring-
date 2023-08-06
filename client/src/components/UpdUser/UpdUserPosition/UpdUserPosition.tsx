import { useState } from "react";
import './UpdUserPosition.css';
import serverURL from "../../../libs/serverApi";

const UpdUserPosition = (props: any) => {
  const [position, setPosition] = useState("");
  const [message, setMessage] = useState("");
  const [category, setCategory] = useState("");
  const position_data = [
    {
      "department": "all",
      "id": 1,
      "position": "CEO",
      "salary": "1000000"
    },
    {
      "department": "all",
      "id": 2,
      "position": "CTO",
      "salary": "650000"
    },
    {
      "department": "Audit",
      "id": 4,
      "position": "CAE",
      "salary": "350000"
    },
    {
      "department": "Audit",
      "id": 5,
      "position": "Auditor",
      "salary": "150000"
    },
    {
      "department": "Artificial Intelligence",
      "id": 6,
      "position": "CAIO",
      "salary": "400000"
    },
    {
      "department": "Artificial Intelligence",
      "id": 7,
      "position": "DS",
      "salary": "200000"
    },
    {
      "department": "new department",
      "id": 9,
      "position": "Sr. SE",
      "salary": "10000000"
    }
  ];

  let handleSubmit = async (e: any) => {
    e.preventDefault();
    try {
      setCategory(category);
      const body = JSON.stringify({
        id: props.id,
        position_new: +position
      })
      console.log(position);

      const requestHeaders: HeadersInit = new Headers();
      requestHeaders.set('Content-Type', 'application/json');
      console.log(JSON.stringify({
        id: props.id,
        position_new: +position
      }))
      let res = await fetch(serverURL + "/api/v1/upd_position_for_person", {
        method: "PUT",
        mode: "cors",
        headers: requestHeaders,
        body: body
      });
      // let resJson = await res.json();
      if (res.status === 200) {
        setPosition("");
        setMessage("Данные успешно изменены");
        // navigate("/home");
      }
      else {
        setMessage("Возникла ошибка при изменение данных");
      }
    } catch (err) {
      console.log(err);
    }
  };

  return (
    <div className="add-user">
      <form className="position-upd" onSubmit={handleSubmit}>
        <select name="category"
          value={category}
          onChange={(e) => setPosition(e.target.value[0])}
          placeholder="Должность"
        >
          {position_data.map((item, i) => (
            <option id={(item.id as unknown) as string} key={i}>{item.id} {item.department} {item.position}</option>
          ))}
        </select>
        <button className="btn-add-user" type="submit">
          Изменить должность
        </button>

        <div className="message">{message ? <p>{message}</p> : null}</div>
      </form>
    </div>
  );
}
export default UpdUserPosition;