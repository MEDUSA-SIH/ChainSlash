import React from 'react';
import AttributionPanel from '../components/AttributionPanel';
import FundFlowGraph from '../components/FundFlowGraph';
import CrossChainView from '../components/CrossChainView';
import CampaignView from '../components/CampaignView';
export default function Cases() {
  return (<div><h2>Cases (priority/status/chain/VASP/risk)</h2>
    <AttributionPanel /><FundFlowGraph /><CrossChainView /><CampaignView /></div>);
}
