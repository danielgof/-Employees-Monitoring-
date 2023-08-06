import { useState } from "react";
import './AddDepartment.css';
import serverURL from "../../libs/serverApi";

const AddDepartment = () => {
  const [position, setPosition] = useState("");
  const [departament, setDepartment] = useState("");
  const [salary, setSalary] = useState("");
  const [message, setMessage] = useState("");

  let handleSubmit = async (e: any) => {
    e.preventDefault();
    try {
      const body = JSON.stringify({
        position: position,
        departament: departament,
        salary: salary
      })

      const requestHeaders: HeadersInit = new Headers();
      requestHeaders.set('Content-Type', 'application/json');
      console.log(JSON.stringify({
        position: position,
        departament: departament,
        salary: salary
      }))
      let res = await fetch(serverURL + "/api/v1/add_position", {
        method: "POST",
        mode: "cors",
        headers: requestHeaders,
        body: body
      });
      // let resJson = await res.json();
      if (res.status === 200) {
        setPosition("");
        setDepartment("");
        setSalary("");
        setMessage("User added to database successfully");
        // navigate("/home");
      }
      else {
        setMessage("Возникла ошибка при добавлении пользователя");
      }
    } catch (err) {
      console.log(err);
    }
  };

  return (
    <div className="add-user">
      <form className="add-user-form" onSubmit={handleSubmit}>
        <input
          type="text"
          value={position}
          placeholder="должность"
          pattern="[0-9]{30}"
          onChange={(e) => setPosition(e.target.value)}
        />
        <input
          type="text"
          value={departament}
          placeholder="отдел"
          pattern="[0-9]{30}"
          onChange={(e) => setDepartment(e.target.value)}
        />
        <input
          type="text"
          value={salary}
          placeholder="зарплата"
          pattern="[0-9]{30}"
          onChange={(e) => setSalary(e.target.value)}
        />

        <button className="btn-add-user" type="submit">
          Добавить должность
        </button>

        <div className="message">{message ? <p>{message}</p> : null}</div>
      </form>
    </div>
  );
}
export default AddDepartment;