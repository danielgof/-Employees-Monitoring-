import { useState } from "react";
import './UpdPhonenum.css';
import serverURL from "../../../libs/serverApi";

const UpdPhonenum = (props: any) => {

  const [phonenumber_new, setNumber] = useState("");
  const [message, setMessage] = useState("");

  let handleSubmit = async (e: any) => {
    e.preventDefault();
    try {
      const body = JSON.stringify({
        phonenumber_old: props.phone,
        phonenumber_new
      })

      const requestHeaders: HeadersInit = new Headers();
      requestHeaders.set('Content-Type', 'application/json');
      console.log(JSON.stringify({
        phonenumber_old: props.phone,
        phonenumber_new
      }))
      let res = await fetch(serverURL + "/api/v1/upd_phone", {
        method: "PUT",
        mode: "cors",
        headers: requestHeaders,
        body: body
      });
      // let resJson = await res.json();
      if (res.status === 200) {
        setNumber("");
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
      <form className="phonenumber-upd" onSubmit={handleSubmit}>
        <input
          type="text"
          value={phonenumber_new}
          placeholder="введите телефон в формате: **********"
          pattern="[0-9]{10}"
          onChange={(e) => setNumber(e.target.value)}
        />
        <button className="btn-add-user" type="submit">
          Изменить номер телефона пользователя
        </button>

        <div className="message">{message ? <p>{message}</p> : null}</div>
      </form>
    </div>
  );
}
export default UpdPhonenum;