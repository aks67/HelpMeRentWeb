import logo from './logo.svg';
import './App.css';
import Title from './components/Title/Title';
import DescriptionBox from './components/DescriptionBox/DescriptionBox';
import MapComponent from './components/MapBox/MapComonent';
import BudgetField from './components/BudgetField/BudgetField';
import RoomSelect from './components/RoomsSelect/RoomSelect';
import DropdownWithFilter from './components/AreasField/AreasField';
import GoButton from './components/GoButton/GoButton';


const MAPBOX_TOKEN = 'pk.eyJ1IjoiYXhrNjcwIiwiYSI6ImNsbjVka2l5cTA2NTcycHF1MnFoNHh5bzgifQ.cSIgT6DWblr6rZMBPU4BWQ'; // Replace with your Mapbox Access Token

function App() {
  return (
    <div className="App">
      <Title text="Help Me Rent" />
      <DescriptionBox
        title="A brief Description"
        description="This is a tool I built for me and my friends to look for a good place"
      />


      <div style={{ display: 'flex', alignItems: 'center', gap:'16px', margin:'16px' }}> 
        <BudgetField />

        <RoomSelect />

        <DropdownWithFilter />
        <GoButton />
      </div>


      <MapComponent mapboxToken={MAPBOX_TOKEN} />
    </div>
  );
}

export default App;
