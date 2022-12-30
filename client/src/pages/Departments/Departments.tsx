import AddDepartment from '../../components/AddDepartment/AddDepartment';
import PositionsInfo from '../../components/PositionsInfo/PositionsInfo';
import './Departments.css';

const Departments = () => {
  return (
    <div className='container'>
      <div className='block'>
        <div className='department'>
          <div>
            <PositionsInfo />
          </div>
          <div>
            <h2>Добавить должность</h2>
              <AddDepartment/>
          </div>
        </div>
      </div>
    </div>
  )
}
export default Departments;