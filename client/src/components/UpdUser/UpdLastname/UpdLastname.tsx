import { useState } from "react";
import './UpdLastname.css';
import serverURL from "../../../libs/serverApi";

const UpdLastname = (props: any) => {

  const [lastname, setName] = useState("");
  const [message, setMessage] = useState("");

  let handleSubmit = async (e: any) => {
    e.preventDefault();
    try {
      const body = JSON.stringify({
        id: props.id,
        lastname_new: lastname
      })

      const requestHeaders: HeadersInit = new Headers();
      requestHeaders.set('Content-Type', 'application/json');
      console.log(JSON.stringify({
        id: props.id,
        lastname_new: lastname
      }))
      let res = await fetch(serverURL + "/api/v1/upd_lastname", {
        method: "PUT",
        mode: "cors",
        headers: requestHeaders,
        body: body
      });
      // let resJson = await res.json();
      if (res.status === 200) {
        setName("");
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
      <form className="lastname-upd" onSubmit={handleSubmit}>
        <input
          type="text"
          value={lastname}
          placeholder="фамилия"
          pattern="[0-9]{30}"
          onChange={(e) => setName(e.target.value)}
        />
        <button className="btn-add-user" type="submit">
          Изменить фамилию пользователя
        </button>

        <div className="message">{message ? <p>{message}</p> : null}</div>
      </form>
    </div>
  );
}
export default UpdLastname;