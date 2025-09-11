---
search:
    exclude: true
---

# pmpd
`pmpd` is a collection of objects for Pd (Pure Data), enabling real-time simulations of physical phenomena. These objects facilitate the creation of dynamic natural systems such as bouncing balls, string oscillations, Brownian motion, chaos theory models, fluid dynamics, sand simulations, gravitational interactions and more. Additionally, `pmpd` allows displacements of physical entities, thus offering a completely dynamic approach of Pd computing.

Utilizing `pmpd`, users can model physical dynamics without the necessity of knowing the comprehensive equation of motions. Simulations require only an understanding of the movement's causality and the structure involved. `pmpd` supplies the foundational objects needed for such simulations and their combination allows the creation of a vast variety of dynamic systems. These object are designed to be used within Pd, a real-time graphical programming environment dedicated to audio signal processing. Pd facilitates the creation of objects, making it particularly suitable for physical modeling. The GEM library focuses on image processing and is employed in `pmpd` examples for visualizing the behavior of physical models. Simulations can be conducted in 1d, 2d or 3d, depending on the objects utilized:


* mass, link and interactor objects are crafted to function cohesively.

* `pmpd`, `pmpd2d` and `pmpd3d` are designed to run simulations as singular entities.

* `pmpd~`, `pmpd2d~` and `pmpd3d~` are intended for audio synthesis applications.
<h2>Contributors</h2>

<div id="libcontributors"></div>

<p align="center">
<i>People who contribute to this project.</i>
</p>


<script>
async function updateList() {
    const repoOwner = 'ch-nry';
    const repoName = 'pd-pmpd';
    try {
        const res = await fetch(`https://api.github.com/repos/${repoOwner}/${repoName}/contributors`);
        const contributors = await res.json();
        const container = document.getElementById('libcontributors');
        contributors.forEach(user => {
            const link = document.createElement('a');
            link.href = `https://github.com/${user.login}`;
            link.target = '_blank';
            const img = document.createElement('img');
            img.src = `https://github.com/${user.login}.png?size=100`;
            img.alt = user.login;
            img.className = 'libavatar';
            link.appendChild(img);
            container.appendChild(link);
        });
    } catch(err) {
        console.error(err);
    }
}
updateList();
</script>


<h2>Objects</h2>

<div class="grid cards" markdown>
- :material-tune: [__iAmbient2D__](../objects/math/iAmbient2D.md) The `iAmbient2D` object simulates ambient interactions in a 2D space, applying constant, random, and damping forces to named "masses." It also handles displacement if a mass moves outside a defined rectangular area.
- :material-tune: [__iAmbient3D__](../objects/physical_modeling/iAmbient3D.md) The `iAmbient3D` object simulates ambient interactions within a 3D space.
- :material-tune: [__iCircle2D__](../objects/physical_modeling/iCircle2D.md) The `iCircle2D` object simulates circular interactions in 2D space, applying various forces and displacements to an interacting mass.
- :material-tune: [__iCircle3D__](../objects/physical_modeling/iCircle3D.md) The `iCircle3D` object simulates the interaction of a named mass with a 3D circular plane.
- :material-tune: [__iCylinder3D__](../objects/physical_modeling/iCylinder3D.md) The `iCylinder3D` object simulates the interaction between a 'mass' and a 3D cylinder.
- :material-tune: [__iLine2D__](../objects/physical_modeling/iLine2D.md) The `iLine2D` object simulates the interaction of a named "mass" with a defined 2D line.
- :material-tune: [__iPlane3D__](../objects/physical_modeling/iPlane3D.md) The `iPlane3D` object simulates the physical interaction between a 3D plane and a specified mass, such as a circle.
- :material-tune: [__iSeg2D__](../objects/physical_modeling/iSeg2D.md) The `iSeg2D` object simulates the physical interaction of a mass with a 2D segment.
- :material-tune: [__iSphere3D__](../objects//iSphere3D.md) The `iSphere3D` object simulates interactions between a "mass" and a 3D spherical boundary.
- :material-tune: [__link__](../objects/math/link.md) The `link` object calculates forces between two masses, simulating a physical connection with configurable rigidity and damping.
- :material-tune: [__link2D__](../objects/physical_modeling/link2D.md) The `link2D` object simulates a physical link between two masses in a 2D space.
- :material-tune: [__link3D__](../objects/physical_modeling/link3D.md) The `link3D` object simulates a physical link between two masses in a 3D environment.
- :material-tune: [__mass__](../objects/physical_modeling/mass.md) The `mass` object simulates a physical mass, calculating its position, velocity, and applied force based on incoming forces and its defined weight.
- :material-tune: [__mass2D__](../objects/physical_modeling/mass2D.md) The `mass2D` object simulates a 2D mass, calculating its position and velocity based on applied forces, weight, and damping.
- :material-tune: [__mass3D__](../objects/math/mass3D.md) The `mass3D` object simulates a mass in a 3D space, calculating its position and velocity based on applied forces, weight, damping, and boundary conditions.
- :material-tune: [__pmpd__](../objects/physical_modeling/pmpd.md) The `pmpd` object in Pure Data implements a mass-spring-damper physical model.
- :material-tune: [__pmpd2d__](../objects/math/pmpd2d.md) The `pmpd2d` object implements a 2D mass-spring-damper physical model, designed for particle-based simulations in Pure Data.
- :material-tune: [__pmpd2d~__](../objects/physical_modeling/pmpd2d~.md) The `pmpd2d~` object performs 2D particle-based physical modeling for audio synthesis.
- :material-tune: [__pmpd3d__](../objects/physical_modeling/pmpd3d.md) The `pmpd3d` object implements 3D physical models based on a mass-spring-damper system.
- :material-tune: [__pmpd3d~__](../objects/physical_modeling/pmpd3d~.md) The `pmpd3d~` object is a 3D particle-based physical modeling engine designed for audio synthesis.
- :material-tune: [__pmpd~__](../objects/physical_modeling/pmpd~.md) The `pmpd~` object is a 1D particle-based physical modeling external for audio synthesis in Pure Data.
- :material-tune: [__tCircle2D__](../objects//tCircle2D.md) The `tCircle2D` object determines if a 2D "mass" is within a specified circular region.
- :material-tune: [__tCircle3D__](../objects//tCircle3D.md) The `tCircle3D` object is designed for testing the 3D position of a "mass" relative to a user-defined circular region.
- :material-tune: [__tCube3D__](../objects/logic/tCube3D.md) The `tCube3D` object determines if a given 3D point (referred to as a "mass") is located within a user-defined 3D bounding box.
- :material-tune: [__tCylinder3D__](../objects/math/tCylinder3D.md) The `tCylinder3D` object defines a 3D cylindrical volume and tests if a given 3D point (referred to as a "mass") is located within its boundaries.
- :material-tune: [__tLine2D__](../objects/math/tLine2D.md) The `tLine2D` object defines a 2D line segment using two points and tracks the position of a "mass" relative to it.
- :material-tune: [__tLink2D__](../objects/physical_modeling/tLink2D.md) The `tLink2D` object calculates properties of a link connecting two masses in a 2D physical simulation.
- :material-tune: [__tLink3D__](../objects/physical_modeling/tLink3D.md) The `tLink3D` object in Pure Data is designed for 3D physical modeling, simulating a link between two masses.
- :material-tune: [__tPlane3D__](../objects/physical_modeling/tPlane3D.md) The `tPlane3D` object simulates interactions involving a 3D plane.
- :material-tune: [__tSeg2D__](../objects//tSeg2D.md) The `tSeg2D` object tests the position of a "mass" relative to a defined 2D line segment.
- :material-tune: [__tSphere3D__](../objects/logic/tSphere3D.md) The `tSphere3D` object performs a spherical test to determine if a "mass" (likely a point or object) is located within a defined 3D spherical region.
- :material-tune: [__tSquare2D__](../objects//tSquare2D.md) The `tSquare2D` object tests if a given 2D mass position falls within a defined square region.
</div>